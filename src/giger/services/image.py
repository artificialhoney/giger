import os
from pathlib import Path
from sys import platform

import piexif
import torch
from compel import Compel
from diffusers import (
    ControlNetModel,
    StableDiffusionControlNetPipeline,
    StableDiffusionImg2ImgPipeline,
    StableDiffusionPipeline,
    UniPCMultistepScheduler,
)
from PIL import Image


class ImageService:
    def __init__(self):
        if torch.cuda.is_available():
            self.cuda = True
        else:
            self.cuda = False

    def txt2img(
        self,
        model,
        prompt,
        negative_prompt,
        output,
        width,
        height,
        loras=[],
        seed=0,
        count=1,
        steps=50,
        name="txt2img",
    ):
        pipeline = self._setup_pipeline(model, StableDiffusionPipeline, loras)
        exif_bytes = self._get_exif_bytes(prompt)
        generator = self._create_generator(seed, count)
        conditioning = self._add_compel(pipeline, prompt)
        images = pipeline(
            prompt_embeds=conditioning,
            generator=generator,
            width=width,
            height=height,
            num_images_per_prompt=count,
            negative_prompt=negative_prompt,
            num_inference_steps=steps,
        )
        self._save_images(images, output, name, seed, exif_bytes)

    def img2img(
        self,
        model,
        prompt,
        negative_prompt,
        output,
        width,
        height,
        image,
        loras=[],
        seed=0,
        count=1,
        steps=50,
        name="img2img",
    ):
        pipeline = self._setup_pipeline(model, StableDiffusionImg2ImgPipeline, loras)
        exif_bytes = self._get_exif_bytes(prompt)
        generator = self._create_generator(seed, count)
        conditioning = self._add_compel(pipeline, prompt)
        images = pipeline(
            prompt_embeds=conditioning,
            generator=generator,
            num_images_per_prompt=count,
            negative_prompt=negative_prompt,
            num_inference_steps=steps,
            image=self._adjust_image(image, width, height),
        )
        self._save_images(images, output, name, seed, exif_bytes)

    def controlnet(
        self,
        model,
        prompt,
        negative_prompt,
        output,
        width,
        height,
        controlnet_model,
        controlnet_conditioning_scale,
        control_guidance_start,
        control_guidance_end,
        image,
        loras=[],
        seed=0,
        count=1,
        steps=50,
        name="controlnet",
    ):
        pipeline = self._setup_pipeline(
            model, StableDiffusionControlNetPipeline, loras, controlnet_model
        )
        exif_bytes = self._get_exif_bytes(prompt)
        generator = self._create_generator(seed, count)
        # speed up diffusion process with faster scheduler and memory optimization
        pipeline.scheduler = UniPCMultistepScheduler.from_config(
            pipeline.scheduler.config
        )
        conditioning = self._add_compel(pipeline, prompt)

        images = pipeline(
            prompt_embeds=conditioning,
            generator=generator,
            width=width,
            height=height,
            num_images_per_prompt=count,
            negative_prompt=negative_prompt,
            num_inference_steps=steps,
            image=self._adjust_image(image, width, height),
            controlnet_conditioning_scale=controlnet_conditioning_scale,
            control_guidance_start=control_guidance_start,
            control_guidance_end=control_guidance_end,
        )
        self._save_images(images, output, name, seed, exif_bytes)

    def _save_images(self, images, output, name, seed, exif_bytes=None):
        for x in range(len(list(images[0]))):
            images[0][x].save(
                os.path.join(
                    Path(output).resolve(),
                    name
                    + "-"
                    + str(x).rjust(3, "0")
                    + "-"
                    + str(seed + x).rjust(6, "0")
                    + ".png",
                ),
                exif=exif_bytes,
            )

    def _create_generator(self, seed, count):
        return [torch.Generator().manual_seed(i + seed) for i in range(count)]

    def _get_exif_bytes(self, prompt):
        exif_ifd = {piexif.ImageIFD.ImageDescription: prompt.encode()}
        exif_dict = {
            "0th": exif_ifd,
            "Exif": {},
            "1st": {},
            "thumbnail": None,
            "GPS": {},
        }
        return piexif.dump(exif_dict)

    def _setup_pipeline(self, model, type, loras=[], controlnet_model=None):
        if controlnet_model:
            controlnet = ControlNetModel.from_pretrained(
                controlnet_model,
                torch_dtype=torch.float16 if self.cuda else torch.float32,
            )
        else:
            controlnet = None
        if self.cuda:
            if controlnet:
                pipeline = type.from_pretrained(
                    model, torch_dtype=torch.float16, controlnet=controlnet
                )
            else:
                pipeline = type.from_pretrained(model, torch_dtype=torch.float16)
            pipeline.to("cuda")
            pipeline.enable_model_cpu_offload()
            pipeline.enable_xformers_memory_efficient_attention()
        else:
            if controlnet:
                pipeline = type.from_pretrained(
                    model, torch_dtype=torch.float32, controlnet=controlnet
                )
            else:
                pipeline = type.from_pretrained(model, torch_dtype=torch.float32)
        for lora_index in range(len(loras)):
            pipeline._lora_scale = loras[lora_index]["scale"]
            pipeline.load_lora_weights(
                loras[lora_index]["model"], weight_name=loras[lora_index]["filename"]
            )
            pipeline._lora_scale = 1.0

        return pipeline

    def _add_compel(self, pipeline, prompt):
        compel = Compel(
            tokenizer=pipeline.tokenizer, text_encoder=pipeline.text_encoder
        )
        return compel.build_conditioning_tensor(prompt)

    def _adjust_image(self, image, width, height, resample=Image.Resampling.LANCZOS):
        im = Image.open(image).convert("RGB")
        im.thumbnail((width, height), resample)
        return im
