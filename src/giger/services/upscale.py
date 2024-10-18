import numpy as np
import torch
from diffusers import StableDiffusionUpscalePipeline
from PIL import Image
from RealESRGAN import RealESRGAN


class UpscaleService:
    def __init__(self):
        if torch.cuda.is_available():
            self.cuda = True
        else:
            self.cuda = False

    def upscale(self, input, output, scale=4):
        device = torch.device("cuda" if self.cuda else "cpu")

        model = RealESRGAN(device, scale=scale)
        model.load_weights("weights/RealESRGAN_x8.pth", download=True)

        image = Image.open(input).convert("RGB")
        sr_image = model.predict(image)

        if "exif" in image.info:
            exif = image.info["exif"]
        else:
            exif = None

        sr_image.save(output, exif=exif) if exif != None else sr_image.save(output)
