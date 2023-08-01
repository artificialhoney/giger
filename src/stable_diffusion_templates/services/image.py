from diffusers import StableDiffusionPipeline
import torch
import piexif
import os

from pathlib import Path

class ImageService:
    def __init__(self, model):
        self.pipeline = StableDiffusionPipeline.from_pretrained(
                model, torch_dtype=torch.float32)
    def txt2img(self, prompt, negative_prompt, output, width, height, seed=0, count=1, steps=50, name="txt2img"):
        exif_ifd = {piexif.ImageIFD.ImageDescription: prompt.encode()}
        exif_dict = {
            "0th": exif_ifd, "Exif": {}, "1st": {},
            "thumbnail": None, "GPS": {}
        }
        exif_bytes = piexif.dump(exif_dict)

        generator = [torch.Generator().manual_seed(i + seed) for i in range(count)]

        images = self.pipeline(prompt, generator=generator, width=width, height=height, num_images_per_prompt=count, negative_prompt=negative_prompt, num_inference_steps=steps)
        for x in range(count):
            images[0][x].save(os.path.join(Path(output).resolve(), name + "-" + str(x).ljust(3, "0") + "-" + seed + ".png"), exif=exif_bytes)