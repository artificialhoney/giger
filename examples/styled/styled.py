#!/usr/bin/env python

import argparse
import logging
import os.path
import sys
from pathlib import Path

from giger.services.image import ImageService
from giger.services.roop import RoopService
from giger.services.upscale import UpscaleService

_logger = logging.getLogger(__name__)

_negative_prompt = "deformed, missing limbs, amputated, pants, shorts, cat ears, bad anatomy, naked, no clothes, disfigured, poorly drawn face, mutation, mutated, ugly, disgusting, blurry, watermark, watermarked, oversaturated, obese, doubled face, b&w, black and white, sepia, nude, frekles, no masks, duplicate image, blur, paintings, sketches, lowres, monochrome, grayscale, bad anatomy, fat, facing away, looking away, tilted head, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, username, blurry, bad feet, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, easy negative, glasses"

_rosagotica_style = "carbon, platinum, dark, black and red silver, night, autumn, roses and thorns, ruby glow, burning, in Transylvania, epic composition, epic proportion, contrast, vibrant color, volumetric lighting, HD"
_demonic_style = "dark, black, japanese, oni, demonic, in the art of Hideki Kamiya, masterpiece, concept art, centered, wide shot, front view, stylish, epic composition, epic proportion, volumetric lighting, HD"
_gothfunk_style = "steel, dark, black, silver, night, spring, gothic and funky, beautiful light, burning, epic composition, epic proportion, contrast, vibrant color, volumetric lighting, HD"
_giger_style = "in the art of H.R. Giger, masterpiece, detailed focus, dynamic angle, 32k UHD resolution, best quality, professional photography, highly detailed, depth of field"
_spawn_style = "in the art of Spawn, comic, masterpiece, detailed focus, 32k UHD resolution, best quality, professional photography, highly detailed"
_mongol_style = "freedom, steel, normad, light, children, sun, spring, flowers, asian, plains, in Mongolia, buddha, epic composition, epic proportion, contrast, vibrant color, volumetric lighting, HD"
_riskart = "masterpiece, concept art, centered, wide shot, front view, wet, rain, night, body tattoo, cute, stylish, sexy pose, epic composition, epic proportion, contrast, vibrant color, volumetric lighting, HD"

_blank_style = ""

_styles = {
    "rosagotica": _rosagotica_style,
    "gothfunk": _gothfunk_style,
    "giger": _giger_style,
    "spawn": _spawn_style,
    "mongol": _mongol_style,
    "demonic": _demonic_style,
    "riskart": _riskart,
    "blank": _blank_style,
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

        parser.add_argument("--upscale", help="Upcale image 4x", action="store_true")

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
            prompts = [args.prompt] * args.size

        for description in prompts:
            _logger.info(f'Generating prompt for "{description}"')
            prompt = (
                "("
                + ", ".join([description, mods, "'" + _styles[args.style] + "'"])
                + ").and()"
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

        if args.upscale:
            _logger.info("Running upscale for generated images")
            upscale_service = UpscaleService()
            for input in Path(os.path.join(args.output, args.batch_name)).glob("*.png"):
                upscale_service.upscale(input, str(input) + ".upscaled.png")

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
