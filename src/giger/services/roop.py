import logging
import os
import urllib.request
from pathlib import Path

import gfpgan
import insightface
import numpy
from huggingface_hub import Repository
from PIL import Image

_logger = logging.getLogger(__name__)


class RoopService:
    def _get_face(self, source, det_size=(640, 640)):
        face_analyser = insightface.app.FaceAnalysis(
            name="buffalo_l", providers=["CPUExecutionProvider"]
        )
        face_analyser.prepare(ctx_id=0, det_size=det_size)

        face = face_analyser.get(source)
        if len(face) == 0 and det_size[0] > 320 and det_size[1] > 320:
            det_size_half = (det_size[0] // 2, det_size[1] // 2)
            return self._get_face(source, det_size=det_size_half)
        try:
            return sorted(face, key=lambda x: x.bbox[0])
        except:
            return None

    def swap(
        self,
        source,
        input,
        output,
        model_name=None,
        gfpgan_path=None,
        enhance=False,
        det_size=(640, 640),
    ):
        roop_dir = os.path.join(str(Path.home()), "roop")
        if not model_name:
            if not os.path.exists(roop_dir):
                Repository(
                    roop_dir, clone_from="ezioruan/inswapper_128.onnx", revision="main"
                )
            model_name = os.path.join(roop_dir, "inswapper_128.onnx")
        if enhance and not gfpgan_path:
            gfpgan_path = os.path.join(roop_dir, "GFPGANv1.4.pth")
            if not os.path.exists(gfpgan_path):
                download_path = "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.4/GFPGANv1.4.pth"
                urllib.request.urlretrieve(download_path, gfpgan_path)
            enhancer = gfpgan.GFPGANer(model_path=gfpgan_path, upscale=1)

        source_image = Image.open(source).convert("RGB")
        input_image = Image.open(input).convert("RGB")
        if "exif" in input_image.info:
            exif = input_image.info["exif"]
        else:
            exif = None
        input_face = self._get_face(numpy.array(input_image), det_size)
        source_face = self._get_face(numpy.array(source_image), det_size)
        if input_face == None:
            _logger.warn('Cannot find face for input "{0}". Exiting.'.format(input))
            return
        if source_face == None:
            _logger.warn('Cannot find face for source "{0}". Exiting.'.format(source))
            return
        model = insightface.model_zoo.get_model(
            model_name, providers=["CPUExecutionProvider"]
        )
        if model == None:
            _logger.warn('Cannot load model "{0}". Exiting.'.format(model_name))
            return

        result = numpy.array(input_image)
        for f in list(input_face):
            result = model.get(result, f, source_face[0])
        if enhance:
            _, _, result = enhancer.enhance(result, paste_back=True)
        result_image = Image.fromarray(result)
        result_image.save(output, exif=exif) if exif != None else result_image.save(
            output
        )
