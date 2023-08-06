from huggingface_hub import Repository
import insightface
import numpy
import os
import glob
from PIL import Image
from pathlib import Path


class RoopService:

    def models(self):
        models_path = os.path.join(self.roop_dir, "*")
        models = glob.glob(models_path)
        models = [os.path.basename(x) for x in models if x.endswith(
            ".onnx") or x.endswith(".pth")]
        return models

    def __init__(self):
        self.roop_dir = os.path.join(str(Path.home()), "roop")
        if not os.path.isdir(self.roop_dir):
            Repository(self.roop_dir, clone_from="henryruhs/roop")

    def get_face(self, source, det_size=(640, 640)):
        face_analyser = insightface.app.FaceAnalysis(
            name="buffalo_l", providers=["CPUExecutionProvider"])
        face_analyser.prepare(ctx_id=0, det_size=det_size)

        face = face_analyser.get(source)
        if len(face) == 0 and det_size[0] > 320 and det_size[1] > 320:
            det_size_half = (det_size[0] // 2, det_size[1] // 2)
            return self.get_face(source, det_size=det_size_half)

        return sorted(face, key=lambda x: x.bbox[0])[0]

    def swap(self, source, input, output, model_name):
        source_image = Image.open(source).convert("RGB")
        input_image = Image.open(input).convert("RGB")
        exif = input_image.info['exif']
        input_face = self.get_face(numpy.array(input_image))
        source_face = self.get_face(numpy.array(source_image))
        model = insightface.model_zoo.get_model(os.path.join(
            self.roop_dir, model_name), providers=["CPUExecutionProvider"])
        result = model.get(numpy.array(input_image),
                           input_face,
                           source_face)
        result_image = Image.fromarray(result)
        result_image.save(output, exif=exif)
