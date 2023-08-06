from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline, StableDiffusionImageVariationPipeline, StableDiffusionControlNetPipeline, ControlNetModel, UniPCMultistepScheduler
import piexif
import os
from sys import platform

from pathlib import Path
from PIL import Image

import torch
from compel import Compel


class ImageService:
    # see https://github.com/facebookresearch/fairseq/issues/2413#issuecomment-1387445867
    def __init__(self):
        if torch.cuda.is_available():
            self.cuda = True
        elif platform == "darwin":
            self.cuda = False

    def txt2img(self, model, prompt, negative_prompt, output, width, height, loras, seed=0, count=1, steps=50, name="txt2img"):
        pipeline = self.setup_pipeline(model, StableDiffusionPipeline, loras)
        exif_bytes = self.get_exif_bytes(prompt)
        generator = self.create_generator(seed, count)
        conditioning = self.add_compel(pipeline, prompt)
        images = pipeline(prompt_embeds=conditioning, generator=generator, width=width, height=height,
                          num_images_per_prompt=count, negative_prompt=negative_prompt, num_inference_steps=steps)
        self.save_images(images, output, name, seed, exif_bytes)

    def controlnet(self, model, prompt, negative_prompt, output, width, height, controlnet_model, controlnet_conditioning_scale, control_guidance_start, control_guidance_end, image, loras, seed=0, count=1, steps=50, name="controlnet"):
        pipeline = self.setup_pipeline(
            model, StableDiffusionControlNetPipeline, loras, controlnet_model)
        exif_bytes = self.get_exif_bytes(prompt)
        generator = self.create_generator(seed, count)
        # speed up diffusion process with faster scheduler and memory optimization
        pipeline.scheduler = UniPCMultistepScheduler.from_config(
            pipeline.scheduler.config)
        conditioning = self.add_compel(pipeline, prompt)
        images = pipeline(prompt_embeds=conditioning, generator=generator, width=width, height=height,
                          num_images_per_prompt=count, negative_prompt=negative_prompt, num_inference_steps=steps, image=Image.open(image).convert("RGB"), controlnet_conditioning_scale=controlnet_conditioning_scale, control_guidance_start=control_guidance_start, control_guidance_end=control_guidance_end)
        self.save_images(images, output, name, seed, exif_bytes)

    def variations(self, output, width, height, image, loras, seed=0, count=1, steps=50, name="img2img"):
        pipeline = self.setup_pipeline(
            "lambdalabs/sd-image-variations-diffusers", StableDiffusionImageVariationPipeline, loras)
        generator = self.create_generator(seed, count)
        images = pipeline(generator=generator, width=width, height=height,
                          num_images_per_prompt=count, num_inference_steps=steps, image=Image.open(image).convert("RGB"))
        self.save_images(images, output, name, seed)

    def img2img(self, model, prompt, negative_prompt, output, width, height, image, loras, seed=0, count=1, steps=50, name="img2img"):
        pipeline = self.setup_pipeline(
            model, StableDiffusionImg2ImgPipeline, loras)
        exif_bytes = self.get_exif_bytes(prompt)
        generator = self.create_generator(seed, count)
        conditioning = self.add_compel(pipeline, prompt)
        images = pipeline(prompt_embeds=conditioning, generator=generator,
                          num_images_per_prompt=count, negative_prompt=negative_prompt, num_inference_steps=steps, image=Image.open(image).convert("RGB").resize((width, height)))
        self.save_images(images, output, name, seed, exif_bytes)

    def save_images(self, images, output, name, seed, exif_bytes=None):
        for x in range(len(list(images[0]))):
            images[0][x].save(os.path.join(Path(output).resolve(
            ), name + "-" + str(x).rjust(3, "0") + "-" + str(seed + x).rjust(6, "0") + ".png"), exif=exif_bytes)

    def create_generator(self, seed, count):
        return [torch.Generator().manual_seed(i + seed) for i in range(count)]

    def get_exif_bytes(self, prompt):
        exif_ifd = {piexif.ImageIFD.ImageDescription: prompt.encode()}
        exif_dict = {
            "0th": exif_ifd, "Exif": {}, "1st": {},
            "thumbnail": None, "GPS": {}
        }
        return piexif.dump(exif_dict)

    def setup_pipeline(self, model, type, loras=[], controlnet_model=None):
        if controlnet_model:
            controlnet = ControlNetModel.from_pretrained(controlnet_model)
        else:
            controlnet = None

        if self.cuda:
            if controlnet:
                pipeline = type.from_pretrained(
                    model, torch_dtype=torch.float16, controlnet=controlnet)
            else:
                pipeline = type.from_pretrained(
                    model, torch_dtype=torch.float16)
            pipeline.to("cuda")
            if type != StableDiffusionImageVariationPipeline:
                pipeline.enable_model_cpu_offload()
                pipeline.enable_xformers_memory_efficient_attention()
        else:
            if controlnet:
                pipeline = type.from_pretrained(
                    model, torch_dtype=torch.float32, controlnet=controlnet)
            else:
                pipeline = type.from_pretrained(
                    model, torch_dtype=torch.float32)
        for lora_index in range(len(loras)):
            pipeline._lora_scale = loras[lora_index]["scale"]
            pipeline.load_lora_weights(
                loras[lora_index]["model"], weight_name=loras[lora_index]["filename"])
            pipeline._lora_scale = 1.0

        return pipeline

    def add_compel(self, pipeline, prompt):
        compel = Compel(tokenizer=pipeline.tokenizer,
                        text_encoder=pipeline.text_encoder)
        return compel.build_conditioning_tensor(prompt)
