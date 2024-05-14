import torch
from diffusers import StableDiffusionUpscalePipeline
from PIL import Image


class UpscaleService:
    def __init__(self):
        if torch.cuda.is_available():
            self.cuda = True
        else:
            self.cuda = False

    def upscale(self, input, output):
        model_id = "stabilityai/stable-diffusion-x4-upscaler"
        if self.cuda:
            pipeline = StableDiffusionUpscalePipeline.from_pretrained(
                model_id, torch_dtype=torch.float16
            )
            pipeline = pipeline.to("cuda")
            pipeline.enable_attention_slicing()
        else:
            pipeline = StableDiffusionUpscalePipeline.from_pretrained(
                model_id, torch_dtype=torch.float32
            )

        input_image = Image.open(input).convert("RGB")
        if "exif" in input_image.info:
            exif = input_image.info["exif"]
        else:
            exif = None
        upscaled_image = pipeline(prompt="", image=input_image).images

        upscaled_image[0].save(output, exif=exif) if exif != None else upscaled_image[
            0
        ].save(output)
