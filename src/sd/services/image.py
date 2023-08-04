from diffusers import StableDiffusionPipeline
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel, UniPCMultistepScheduler
from diffusers import StableDiffusionImg2ImgPipeline
from diffusers.utils import load_image
import piexif
import os
from sys import platform

from pathlib import Path
from PIL import Image

# see https://github.com/facebookresearch/fairseq/issues/2413#issuecomment-1387445867
import torch

if platform == "darwin":
    torch.set_default_dtype(torch.float32)

class ImageService:
    def txt2img(self, model, prompt, negative_prompt, output, width, height, seed=0, count=1, steps=50, name="txt2img"):
        pipeline = StableDiffusionPipeline.from_pretrained(
            model)
        exif_ifd = {piexif.ImageIFD.ImageDescription: prompt.encode()}
        exif_dict = {
            "0th": exif_ifd, "Exif": {}, "1st": {},
            "thumbnail": None, "GPS": {}
        }
        exif_bytes = piexif.dump(exif_dict)

        generator = [torch.Generator().manual_seed(i + seed) for i in range(count)]

        images = pipeline(prompt, generator=generator, width=width, height=height,
                               num_images_per_prompt=count, negative_prompt=negative_prompt, num_inference_steps=steps)
        for x in range(count):
            images[0][x].save(os.path.join(Path(output).resolve(
            ), name + "-" + str(x).rjust(3, "0") + "-" + str(seed) + ".png"), exif=exif_bytes)

    def controlnet(self, model, prompt, negative_prompt, output, width, height, controlnet_model, image, seed=0, count=1, steps=50, name="controlnet"):
        controlnet = ControlNetModel.from_pretrained(controlnet_model)
        pipeline = StableDiffusionControlNetPipeline.from_pretrained(
            model, controlnet=controlnet
        )

        # speed up diffusion process with faster scheduler and memory optimization
        pipeline.scheduler = UniPCMultistepScheduler.from_config(pipeline.scheduler.config)
        # remove following line if xformers is not installed
        # pipeline.enable_xformers_memory_efficient_attention()

        # pipeline.enable_model_cpu_offload()


        exif_ifd = {piexif.ImageIFD.ImageDescription: prompt.encode()}
        exif_dict = {
            "0th": exif_ifd, "Exif": {}, "1st": {},
            "thumbnail": None, "GPS": {}
        }
        exif_bytes = piexif.dump(exif_dict)

        generator = [torch.Generator().manual_seed(i + seed) for i in range(count)]
        images = pipeline(prompt, generator=generator, width=width, height=height,
                        num_images_per_prompt=count, negative_prompt=negative_prompt, num_inference_steps=steps, image=Image.open(image).convert("RGB"))

        for x in range(count):
            images[0][x].save(os.path.join(Path(output).resolve(
            ), name + "-" + str(x).rjust(3, "0") + "-" + str(seed) + ".png"), exif=exif_bytes)

    def img2img(self, model, prompt, negative_prompt, output, width, height, image, seed=0, count=1, steps=50, name="img2img"):
        pipeline = StableDiffusionImg2ImgPipeline.from_pretrained(model)

        exif_ifd = {piexif.ImageIFD.ImageDescription: prompt.encode()}
        exif_dict = {
            "0th": exif_ifd, "Exif": {}, "1st": {},
            "thumbnail": None, "GPS": {}
        }
        exif_bytes = piexif.dump(exif_dict)

        generator = [torch.Generator().manual_seed(i + seed) for i in range(count)]

        images = pipeline(prompt, generator=generator,
                               num_images_per_prompt=count, negative_prompt=negative_prompt, num_inference_steps=steps, image=Image.open(image).convert("RGB").resize((width, height)))
        for x in range(count):
            images[0][x].save(os.path.join(Path(output).resolve(
            ), name + "-" + str(x).rjust(3, "0") + "-" + str(seed) + ".png"), exif=exif_bytes)