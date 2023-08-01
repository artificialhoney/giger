from diffusers import DiffusionPipeline
import torch
import piexif

from pathlib import Path

class ImageService:
    def __init__(self, model):
        self.pipeline = DiffusionPipeline.from_pretrained(
                model, torch_dtype=torch.float32)
    def txt2img(self, prompt, output, width, height):
        exif_ifd = {piexif.ImageIFD.ImageDescription: prompt.encode()}
        exif_dict = {
            "0th": exif_ifd, "Exif": {}, "1st": {},
            "thumbnail": None, "GPS": {}
        }
        exif_bytes = piexif.dump(exif_dict)

        image = self.pipeline(prompt, width=width, height=height).images[0]
        image.save(Path(output).resolve(), exif=exif_bytes)