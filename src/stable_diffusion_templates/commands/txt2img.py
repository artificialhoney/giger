from ..services.image import ImageService
import logging

_logger = logging.getLogger(__name__)


class Txt2ImgCommand:
    def __init__(self, parser):
        self.parser = parser.add_parser(
            "txt2img", help="Generate generate image from prompt")
        self.parser.add_argument(
            "--model", help="The Stable Diffusion model to use", default="Lykon/DreamShaper")
        self.parser.add_argument(
            "--prompt", help="The text prompt", required=True)
        self.parser.add_argument(
            "--output", help="The output image file", required=True)
        self.parser.add_argument("--width", default=768, type=int)
        self.parser.add_argument("--height", default=432, type=int)

    def run(self, args):
        _logger.info("Creating image for '{0}'".format(args.prompt))
        self.service = ImageService(args.model)
        self.service.txt2img(args.prompt, args.output, args.width, args.height)
