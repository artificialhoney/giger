import logging
import os
import pathlib
import random
import sys

_logger = logging.getLogger(__name__)


class ImageCommand:
    def __init__(self, parser):
        self.parser = parser.add_parser(
            "image", help="Generate generate image from prompt"
        )
        self.parser.add_argument("prompt", help="The text prompt", nargs="*")

        self.parser.add_argument(
            "--model",
            help="The Stable Diffusion model to use",
            default="Lykon/DreamShaper",
        )
        self.parser.add_argument("--negative_prompt", help="The negative text prompt")
        self.parser.add_argument("-i", "--input", help="The input image")
        self.parser.add_argument(
            "-o", "--output", help="The output image folder", required=True
        )
        self.parser.add_argument(
            "--name", help="The name of the generated image", default="image"
        )
        self.parser.add_argument("--width", default=768, type=int)
        self.parser.add_argument("--height", default=432, type=int)
        self.parser.add_argument("--batch_size", default=1, type=int)
        self.parser.add_argument("--inference_steps", default=50, type=int)
        self.parser.add_argument("--seed", type=int)
        self.parser.add_argument(
            "--controlnet_model", help="The ControlNet model to use"
        )
        self.parser.add_argument(
            "--controlnet_conditioning_scale",
            help="The ControlNet conditioning scale",
            type=float,
            default=1.0,
        )
        self.parser.add_argument(
            "--control_guidance_start",
            help="The ControlNet control guidance start",
            type=float,
            default=0.0,
        )
        self.parser.add_argument(
            "--control_guidance_end",
            help="The ControlNet control guidance end",
            type=float,
            default=1.0,
        )
        self.parser.add_argument(
            "--lora_model", help="A LoRA model to use", nargs="*", default=[]
        )
        self.parser.add_argument(
            "--lora_filename", help="The LoRA file name", nargs="*", default=[]
        )
        self.parser.add_argument(
            "--lora_scale", help="The LoRA scale", nargs="*", default=[], type=float
        )
        self.parser.add_argument(
            "--inversion_model",
            help="A textual inversion model to use",
            nargs="*",
            default=[],
        )
        self.parser.add_argument(
            "--inversion_filename",
            help="The textual inversion file name",
            nargs="*",
            default=[],
        )
        self.parser.add_argument(
            "--inversion_token",
            help="The textual inversion token",
            nargs="*",
            default=[],
        )
        self.parser.add_argument(
            "--bypass_safety", help="Bypass Safety (NSFW)", action="store_true"
        )

    def execute(self, args):
        if args.seed == None:
            seed = random.randint(0, 1000000)
        else:
            seed = args.seed

        if not sys.stdin.isatty():
            args.prompt = sys.stdin.read().splitlines() + args.prompt
        prompt = ", ".join(args.prompt)

        loras = []
        for index, lora_model in enumerate(args.lora_model):
            loras.append(
                {
                    "model": lora_model,
                    "filename": args.lora_filename[index]
                    if index < len(args.lora_filename)
                    else None,
                    "scale": args.lora_scale[index]
                    if index < len(args.lora_scale)
                    else 1.0,
                }
            )

        inversions = []
        for index, inversion_model in enumerate(args.inversion_model):
            inversions.append(
                {
                    "model": inversion_model,
                    "filename": args.inversion_filename[index]
                    if index < len(args.inversion_filename)
                    else None,
                    "token": args.inversion_token[index]
                    if index < len(args.inversion_token)
                    else None,
                }
            )

        _logger.info('Creating image for "{0}"'.format(prompt))

        from ..services.image import ImageService

        self.service = ImageService()

        pathlib.Path(args.output).mkdir(parents=True, exist_ok=True)

        if args.input != None:
            if args.controlnet_model != None:
                self.service.controlnet(
                    args.model,
                    prompt,
                    args.negative_prompt,
                    args.output,
                    args.width,
                    args.height,
                    args.controlnet_model,
                    args.controlnet_conditioning_scale,
                    args.control_guidance_start,
                    args.control_guidance_end,
                    args.input,
                    loras,
                    inversions,
                    seed,
                    args.batch_size,
                    args.inference_steps,
                    args.name,
                    args.bypass_safety,
                )
            else:
                self.service.img2img(
                    args.model,
                    prompt,
                    args.negative_prompt,
                    args.output,
                    args.width,
                    args.height,
                    args.input,
                    loras,
                    inversions,
                    seed,
                    args.batch_size,
                    args.inference_steps,
                    args.name,
                    args.bypass_safety,
                )
        else:
            self.service.txt2img(
                args.model,
                prompt,
                args.negative_prompt,
                args.output,
                args.width,
                args.height,
                loras,
                inversions,
                seed,
                args.batch_size,
                args.inference_steps,
                args.name,
                args.bypass_safety,
            )
