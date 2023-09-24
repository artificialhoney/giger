#!/usr/bin/env python

import argparse
import logging
import os.path
import sys
from pathlib import Path

from giger.services.image import ImageService
from giger.services.prompt import PromptService
from giger.services.roop import RoopService

_logger = logging.getLogger(__name__)

_negative_prompt = "deformed, missing limbs, amputated, pants, shorts, cat ears, bad anatomy, naked, no clothes, disfigured, poorly drawn face, mutation, mutated, ugly, disgusting, blurry, watermark, watermarked, oversaturated, obese, doubled face, b&w, black and white, sepia, nude, frekles, no masks, duplicate image, blur, paintings, sketches, lowres, monochrome, grayscale, bad anatomy, fat, facing away, looking away, tilted head, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, username, blurry, bad feet, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, easy negative, glasses"


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

        parser = argparse.ArgumentParser(prog="batch", description="Simple batch tool")

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
            "-a",
            "--artist",
            help="Artist name",
            type=str,
            default="H.R. Giger",
        )
        parser.add_argument(
            "-t",
            "--time",
            help="Time description",
            type=str,
            default="Ancient",
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
        parser.add_argument("-c", "--count", help="Batch count", default=10, type=int)
        parser.add_argument("-s", "--seed", help="Batch seed", type=int, default=0)

        parser.add_argument(
            "-d",
            "--dimension",
            help="Image dimension",
            type=tuple_type,
            default=(768, 432),
        )
        parser.add_argument("-l", "--lora", help="LoRa scale", type=float, default=0.75)
        parser.add_argument(
            "-p",
            "--prompts",
            help="Prompts txt file",
            required=True,
            metavar="FILE",
            type=lambda x: is_valid_file(parser, x),
        )

        parser.add_argument(
            "-n",
            "--negative_prompt",
            help="Negative prompt",
            type=str,
            default=_negative_prompt,
        )
        parser.add_argument("-f", "--face", help="Face input image", required=False)

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

        prompt_service = PromptService()
        image_service = ImageService()
        path = os.path.join(args.output, args.batch_name)
        Path(path).mkdir(parents=True, exist_ok=True)
        seed = args.seed
        for description in args.prompts:
            _logger.info(f'Generating prompt for "{description}"')
            prompt = prompt_service.generate(
                description=[description],
                time=args.time,
                type="Comic Book",
                art_style=["Concept Art"],
                artist=[args.artist],
                realism=["Photorealistic"],
                rendering_engine=["Octane Render"],
                lightning_angle=["Back Light"],
                lightning_style=["Cinematic"],
                camera_position=["Full-Body Shot"],
                camera_style=["Long Exposure"],
                resolution=["8k"],
                compel_style="subtle",
            )
            _logger.info(f'Running batch for "{prompt}"')
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
                50,
                args.batch_name,
            )
            seed += args.count

        if args.face:
            _logger.info(
                f'Running roop for generated images with face from "{args.face}"'
            )
            roop_service = RoopService()
            for input in Path(os.path.join(args.output, args.batch_name)).glob("*.png"):
                roop_service.swap(args.face, input, str(input) + ".swapped.png")


def run():
    CharacterCLI().run(sys.argv[1:])


if __name__ == "__main__":
    run()
