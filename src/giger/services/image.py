import os
from pathlib import Path

import piexif
import torch
from diffusers import (
    AutoPipelineForImage2Image,
    AutoPipelineForText2Image,
    ControlNetModel,
    DPMSolverMultistepScheduler,
    StableDiffusionControlNetPipeline,
)
from PIL import Image


def _bypass_safety(images, clip_input):
    if len(images.shape) == 4:
        num_images = images.shape[0]
        return images, [False] * num_images
    else:
        return images, False


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
        inversions=[],
        seed=0,
        count=1,
        steps=50,
        name="txt2img",
        bypass_safety=False,
    ):
        pipeline = self._setup_pipeline(
            model, AutoPipelineForText2Image, loras, inversions
        )

        if bypass_safety:
            pipeline.safety_checker = _bypass_safety

        exif_bytes = self._get_exif_bytes(prompt)
        generator = self._create_generator(seed, count)

        images = pipeline(
            prompt=prompt,
            generator=generator,
            width=width,
            height=height,
            num_images_per_prompt=count,
            negative_prompt=negative_prompt,
            num_inference_steps=steps,
            cross_attention_kwargs={"scale": 1.0},
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
        inversions=[],
        seed=0,
        count=1,
        steps=50,
        name="img2img",
        bypass_safety=False,
    ):
        pipeline = self._setup_pipeline(
            model, AutoPipelineForImage2Image, loras, inversions
        )

        if bypass_safety:
            pipeline.safety_checker = _bypass_safety

        exif_bytes = self._get_exif_bytes(prompt)
        generator = self._create_generator(seed, count)

        images = pipeline(
            prompt=prompt,
            generator=generator,
            num_images_per_prompt=count,
            negative_prompt=negative_prompt,
            num_inference_steps=steps,
            image=self._adjust_image(image, width, height),
            cross_attention_kwargs={"scale": 1.0},
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
        inversions=[],
        seed=0,
        count=1,
        steps=50,
        name="controlnet",
        bypass_safety=False,
    ):
        pipeline = self._setup_pipeline(
            model,
            StableDiffusionControlNetPipeline,
            loras,
            inversions,
            controlnet_model,
        )

        if bypass_safety:
            pipeline.safety_checker = _bypass_safety

        exif_bytes = self._get_exif_bytes(prompt)
        generator = self._create_generator(seed, count)

        images = pipeline(
            prompt=prompt,
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
            cross_attention_kwargs={"scale": 1.0},
        )
        self._save_images(images, output, name, seed, exif_bytes)

    def _save_images(self, images, output, name, seed, exif_bytes=None):
        for x in range(len(list(images[0]))):
            p = os.path.join(
                Path(output).resolve(),
                name + "-" + str(seed + x).rjust(6, "0") + ".png",
            )

            images[0][x].save(
                p,
                exif=exif_bytes,
            )

    def _create_generator(self, seed, count):
        if self.cuda:
            return [
                torch.Generator(device="cuda").manual_seed(i + seed)
                for i in range(count)
            ]
        else:
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

    def _setup_pipeline(
        self, model, type, loras=[], inversions=[], controlnet_model=None
    ):
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

        if len(loras) > 0:
            adapters = []
            for lora_index, lora in enumerate(loras):
                adapter = "lora" + str(lora_index)
                adapters += [adapter]
                pipeline.load_lora_weights(
                    lora["model"],
                    weight_name=lora["filename"],
                    adapter_name=adapter,
                )

            pipeline.set_adapters(adapters, adapter_weights=[x["scale"] for x in loras])

        if len(inversions) > 0:
            for inversion in list(inversions):
                pipeline.load_textual_inversion(
                    inversion["model"],
                    weight_name=inversion["filename"],
                    token=inversion["token"],
                )

        pipeline.scheduler = DPMSolverMultistepScheduler.from_config(
            pipeline.scheduler.config
        )

        return pipeline

    def _adjust_image(self, image, width, height, resample=Image.Resampling.LANCZOS):
        im = Image.open(image).convert("RGB")
        im.thumbnail((width, height), resample)
        return im
