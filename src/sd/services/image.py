from diffusers import StableDiffusionPipeline
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel, UniPCMultistepScheduler
from diffusers import StableDiffusionImg2ImgPipeline
import piexif
import os
from sys import platform

from pathlib import Path
from PIL import Image

import torch


class ImageService:
    # see https://github.com/facebookresearch/fairseq/issues/2413#issuecomment-1387445867
    def __init__(self):
        if torch.cuda.is_available():
            self.cuda = True
        elif platform == "darwin":
            self.cuda = False

    def txt2img(self, model, prompt, negative_prompt, output, width, height, seed=0, count=1, steps=50, name="txt2img"):
        if self.cuda:
            pipeline = StableDiffusionPipeline.from_pretrained(
                model, torch_dtype=torch.float16)
            pipeline.to("cuda")
            pipeline.enable_model_cpu_offload()
            pipeline.enable_xformers_memory_efficient_attention()
        else:
            pipeline = StableDiffusionPipeline.from_pretrained(
                model, torch_dtype=torch.float32)

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
            ), name + "-" + str(x).rjust(3, "0") + "-" + str(seed + x).rjust(6, "0") + ".png"), exif=exif_bytes)

    def controlnet(self, model, prompt, negative_prompt, output, width, height, controlnet_model, controlnet_conditioning_scale, control_guidance_start, control_guidance_end, image, seed=0, count=1, steps=50, name="controlnet"):
        controlnet = ControlNetModel.from_pretrained(controlnet_model)

        if self.cuda:
            pipeline = StableDiffusionControlNetPipeline.from_pretrained(
            model, controlnet=controlnet, torch_dtype=torch.float16)
            pipeline.to("cuda")
            pipeline.enable_model_cpu_offload()
            pipeline.enable_xformers_memory_efficient_attention()
        else:
            pipeline = StableDiffusionControlNetPipeline.from_pretrained(
            model, controlnet=controlnet, torch_dtype=torch.float32)

        # speed up diffusion process with faster scheduler and memory optimization
        pipeline.scheduler = UniPCMultistepScheduler.from_config(
            pipeline.scheduler.config)

        exif_ifd = {piexif.ImageIFD.ImageDescription: prompt.encode()}
        exif_dict = {
            "0th": exif_ifd, "Exif": {}, "1st": {},
            "thumbnail": None, "GPS": {}
        }
        exif_bytes = piexif.dump(exif_dict)

        generator = [torch.Generator().manual_seed(i + seed) for i in range(count)]
        images = pipeline(prompt, generator=generator, width=width, height=height,
                          num_images_per_prompt=count, negative_prompt=negative_prompt, num_inference_steps=steps, image=Image.open(image).convert("RGB"), controlnet_conditioning_scale=controlnet_conditioning_scale, control_guidance_start=control_guidance_start, control_guidance_end=control_guidance_end)

        for x in range(count):
            images[0][x].save(os.path.join(Path(output).resolve(
            ), name + "-" + str(x).rjust(3, "0") + "-" + str(seed + x).rjust(6, "0") + ".png"), exif=exif_bytes)

    def img2img(self, model, prompt, negative_prompt, output, width, height, image, seed=0, count=1, steps=50, name="img2img"):
        pipeline = StableDiffusionImg2ImgPipeline.from_pretrained(model)

        if self.cuda:
            pipeline = StableDiffusionImg2ImgPipeline.from_pretrained(
            model, torch_dtype=torch.float16)
            pipeline.to("cuda")
            pipeline.enable_model_cpu_offload()
            pipeline.enable_xformers_memory_efficient_attention()
        else:
            pipeline = StableDiffusionImg2ImgPipeline.from_pretrained(
            model, torch_dtype=torch.float32)

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
            ), name + "-" + str(x).rjust(3, "0") + "-" + str(seed + x).rjust(6, "0") + ".png"), exif=exif_bytes)
