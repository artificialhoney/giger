from ..services.image import ImageService
import logging
import os
import pathlib
import random
import io
import sys

_logger = logging.getLogger(__name__)


class Txt2ImgCommand:
    def __init__(self, parser):
        self.parser = parser.add_parser(
            "txt2img", help="Generate generate image from prompt")
        self.parser.add_argument(
            "prompt", help="The text prompt", nargs="?", default=(None if sys.stdin.isatty() else sys.stdin))

        self.parser.add_argument(
            "--model", help="The Stable Diffusion model to use", default="Lykon/DreamShaper")
        self.parser.add_argument(
            "--negative_prompt", help="The negative text prompt")
        self.parser.add_argument(
            "--output", help="The output image folder", required=True)
        self.parser.add_argument(
        "--name", help="The name of the generated image", default="txt2img")
        self.parser.add_argument("--width", default=768, type=int)
        self.parser.add_argument("--height", default=432, type=int)
        self.parser.add_argument("--batch_size", default=1, type=int)
        self.parser.add_argument("--batch_count", default=1, type=int)
        self.parser.add_argument("--inference_steps", default=50, type=int)
        self.parser.add_argument("--seed", type=int)

    def run(self, args):
        _logger.info("Creating image for '{0}'".format(args.prompt))
        self.service = ImageService(args.model)

        if args.seed == None:
            seed = random.randint(0, 1000)
        else:
            seed = args.seed

        if isinstance(args.prompt, io.TextIOWrapper):
            prompt = args.prompt.read()
        else:
            prompt = args.prompt


        for x in range(args.batch_size):
            path = os.path.join(args.output, args.name)
            pathlib.Path(path).mkdir(parents=True, exist_ok=True)
            self.service.txt2img(prompt, args.negative_prompt, path, args.width, args.height, seed + x, args.batch_count, args.inference_steps, args.name + "-" + str(x).rjust(3, "0"))
