#!/usr/bin/env python

import argparse
import logging
import os.path
import sys
from pathlib import Path

from giger.services.image import ImageService
from giger.services.prompt import PromptService
from giger.services.roop import RoopService
from giger.services.upscale import UpscaleService

_logger = logging.getLogger(__name__)

# https://openaijourney.com/fix-hands-in-stable-diffusion/
# _negative_prompt = "The artwork avoids the pitfalls of bad art, such as ugly and deformed eyes and faces, poorly drawn, blurry, and disfigured bodies with extra limbs and close-ups that look weird. It also avoids other common issues such as watermarking, text errors, missing fingers or digits, cropping, poor quality, and JPEG artifacts. The artwork is free of signature or watermark and avoids framing issues. The hands are not deformed, the eyes are not disfigured, and there are no extra bodies or limbs. The artwork is not blurry, out of focus, or poorly drawn, and the proportions are not bad or deformed. There are no mutations, missing limbs, or floating or disconnected limbs. The hands and neck are not malformed, and there are no extra heads or out-of-frame elements. The artwork is not low-res or disgusting and is a well-drawn, highly detailed, and beautiful rendering."
_negative_prompt = "EasyNegative"


_standard_style = {
    "resolution": ["8K"],
    "realism": ["Ultra Photoreal", "Ultra Detailed"],
    "type": "Photograph",
    "lightning_style": ["Cinematic", "Volumetric"],
    "camera_position": ["Cinematic Still Shot"],
    "compel_style": "subtle",
}

_styles = {
    "standard": _standard_style,
    "blank": {},
}


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, "r")  # return an open file handle


def tuple_type(strings):
    strings = strings.replace("(", "").replace(")", "")
    mapped_int = map(int, strings.split(","))
    return tuple(mapped_int)


class CharacterCLI:
    def parse_args(self, args):
        """
        Parse command line parameters
        """

        parser = argparse.ArgumentParser(prog="styled", description="Styled tooling")

        parser.add_argument(
            "-v",
            "--verbose",
            dest="loglevel",
            help="set loglevel to INFO",
            action="store_const",
            const=logging.INFO,
        )
        parser.add_argument(
            "-vv",
            "--very-verbose",
            dest="loglevel",
            help="set loglevel to DEBUG",
            action="store_const",
            const=logging.DEBUG,
        )
        parser.add_argument(
            "-m",
            "--model",
            help="The Stable Diffusion model to use",
            default="Lykon/DreamShaper",
        )
        parser.add_argument(
            "-o", "--output", help="Batch output", type=str, required=True
        )
        parser.add_argument(
            "-b",
            "--batch_name",
            help="Batch name",
            type=str,
            default="batch",
        )
        parser.add_argument("--count", help="Batch count", default=4, type=int)
        parser.add_argument("--size", help="Batch size", default=10, type=int)
        parser.add_argument(
            "--scale", help="Scale image factor", type=int, required=False
        )
        parser.add_argument("--mod", nargs="*", action="append", default=[])
        parser.add_argument("-s", "--seed", help="Batch seed", type=int, default=0)

        parser.add_argument(
            "-d",
            "--dimension",
            help="Image dimension",
            type=tuple_type,
            default=(768, 432),
        )
        parser.add_argument("-l", "--lora", help="LoRa scale", type=float, default=1.0)
        parser.add_argument(
            "-p", "--prompt", help="Prompts txt file or string", required=True, type=str
        )

        parser.add_argument(
            "-n",
            "--negative_prompt",
            help="Negative prompt",
            type=str,
            default=_negative_prompt,
        )
        parser.add_argument("-f", "--face", help="Face input image", required=False)
        parser.add_argument("-ef", "--enhance_face", action="store_true")

        parser.add_argument("--net", help="ControlNet input image", required=False)
        parser.add_argument(
            "--netmix",
            help="Net mix strength",
            type=float,
            default=0.75,
        )

        parser.add_argument(
            "--netstart",
            help="ControlNet start",
            type=float,
            default=0.0,
        )

        parser.add_argument(
            "--netend",
            help="ControlNet end",
            type=float,
            default=1.0,
        )

        parser.add_argument("--steps", default=30, type=int)

        parser.add_argument(
            "--bypass_safety",
            help="Bypass Safety (NSFW)",
            action="store_true",
        )

        parser.add_argument("style", choices=_styles.keys(), default="blank")

        return parser.parse_args(args)

    def setup_logging(self, loglevel):
        """
        Setup basic logging

        Args:
            loglevel (int): minimum loglevel for emitting messages
        """
        logformat = "[%(asctime)s] %(levelname)s - %(name)s - %(message)s"
        logging.basicConfig(
            level=loglevel,
            stream=sys.stdout,
            format=logformat,
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    def run(self, args):
        _logger.info("Starting batch")
        args = self.parse_args(args)
        self.setup_logging(args.loglevel)

        from diffusers import utils

        if args.loglevel == logging.DEBUG:
            utils.logging.set_verbosity_debug()
        elif args.loglevel == logging.INFO:
            utils.logging.set_verbosity_info()
        else:
            utils.logging.set_verbosity_error()

        image_service = ImageService()
        prompt_service = PromptService()
        path = os.path.join(args.output, args.batch_name)
        Path(path).mkdir(parents=True, exist_ok=True)
        seed = args.seed
        mods = [item for sublist in args.mod for item in sublist]
        mods = ", ".join(map(lambda x: "'" + x + "'", mods))

        # Check if the file exists
        if os.path.exists(args.prompt):
            text_file = open(args.prompt, "r")
            prompts = text_file.readlines()
        else:
            prompts = ["'" + args.prompt + "'"] * args.size

        for description in prompts:
            _logger.info(f'Generating prompt for "{description}"')
            prompt = prompt_service.generate(
                description=[description, mods], **_styles[args.style]
            )
            _logger.info(f'Running batch for "{prompt}"')

            if args.net:
                image_service.controlnet(
                    args.model,
                    prompt,
                    args.negative_prompt,
                    path,
                    args.dimension[0],
                    args.dimension[1],
                    "lllyasviel/sd-controlnet-hed",
                    args.netmix,
                    args.netstart,
                    args.netend,
                    args.net,
                    [
                        {
                            "model": "OedoSoldier/detail-tweaker-lora",
                            "filename": "add_detail.safetensors",
                            "scale": args.lora,
                        }
                    ],
                    seed,
                    args.count,
                    args.steps,
                    args.batch_name,
                    args.bypass_safety,
                )
            else:
                image_service.txt2img(
                    args.model,
                    prompt,
                    args.negative_prompt,
                    path,
                    args.dimension[0],
                    args.dimension[1],
                    [
                        {
                            "model": "OedoSoldier/detail-tweaker-lora",
                            "filename": "add_detail.safetensors",
                            "scale": args.lora,
                        }
                    ],
                    seed,
                    args.count,
                    args.steps,
                    args.batch_name,
                    args.bypass_safety,
                )
            seed += args.count

        if args.face:
            _logger.info(
                f'Running roop for generated images with face from "{args.face}"'
            )
            roop_service = RoopService()
            for input in Path(os.path.join(args.output, args.batch_name)).glob("*.png"):
                roop_service.swap(
                    args.face,
                    input,
                    str(input) + ".swapped.png",
                    enhance=args.enhance_face,
                )

        if args.scale:
            _logger.info(f'Running upscale for generated images with "{args.scale}"')
            upscale_service = UpscaleService()
            for input in Path(os.path.join(args.output, args.batch_name)).glob("*.png"):
                upscale_service.upscale(input, str(input) + ".upscaled.png", args.scale)


def run():
    CharacterCLI().run(sys.argv[1:])


if __name__ == "__main__":
    run()
