import glob
import logging
import os
from pathlib import Path

import insightface
import numpy
from huggingface_hub import Repository
from PIL import Image

_logger = logging.getLogger(__name__)


class RoopService:
    def get_face(self, source, det_size=(640, 640)):
        face_analyser = insightface.app.FaceAnalysis(
            name="buffalo_l", providers=["CPUExecutionProvider"]
        )
        face_analyser.prepare(ctx_id=0, det_size=det_size)

        face = face_analyser.get(source)
        if len(face) == 0 and det_size[0] > 320 and det_size[1] > 320:
            det_size_half = (det_size[0] // 2, det_size[1] // 2)
            return self.get_face(source, det_size=det_size_half)
        try:
            return sorted(face, key=lambda x: x.bbox[0])[0]
        except:
            return None

    def swap(self, source, input, output, model_name=None):
        if not model_name:
            roop_dir = os.path.join(str(Path.home()), "roop")
            if not os.path.igigerir(roop_dir):
                Repository(roop_dir, clone_from="henryruhs/roop")
            model_name = os.path.join(roop_dir, "inswapper_128.onnx")
        source_image = Image.open(source).convert("RGB")
        input_image = Image.open(input).convert("RGB")
        exif = input_image.info["exif"]
        input_face = self.get_face(numpy.array(input_image))
        source_face = self.get_face(numpy.array(source_image))
        if input_face == None:
            _logger.warn("Cannot find face for input '{0}'. Exiting.".format(input))
            return
        if source_face == None:
            _logger.warn("Cannot find face for source '{0}'. Exiting.".format(source))
            return
        model = insightface.model_zoo.get_model(
            model_name, providers=["CPUExecutionProvider"]
        )
        result = model.get(numpy.array(input_image), input_face, source_face)
        result_image = Image.fromarray(result)
        result_image.save(output, exif=exif)
