import logging
import os
import sys

from ..services.prompt import PromptService

_logger = logging.getLogger(__name__)


class PromptCommand:
    def __init__(self, parser):
        self.parser = parser.add_parser("prompt", help="Generate prompt")
        self.parser.add_argument("description", nargs="*")
        self.parser.add_argument("--time", choices=PromptService.times())
        self.parser.add_argument("--type", choices=PromptService.types())
        self.parser.add_argument("--background_color")
        self.parser.add_argument(
            "--art_style", choices=PromptService.art_styles(), nargs="*"
        )
        self.parser.add_argument("--artist", choices=PromptService.artists(), nargs="*")
        self.parser.add_argument(
            "--realism", choices=PromptService.realisms(), nargs="*"
        )
        self.parser.add_argument(
            "--rendering_engine", choices=PromptService.rendering_engines(), nargs="*"
        )
        self.parser.add_argument(
            "--lightning_angle", choices=PromptService.lightning_angles(), nargs="*"
        )
        self.parser.add_argument(
            "--lightning_style", choices=PromptService.lightning_styles(), nargs="*"
        )
        self.parser.add_argument(
            "--camera_position", choices=PromptService.camera_positions(), nargs="*"
        )
        self.parser.add_argument("--camera", choices=PromptService.cameras(), nargs="*")
        self.parser.add_argument("--style", choices=PromptService.styles(), nargs="*")
        self.parser.add_argument(
            "--composition", choices=PromptService.compositions(), nargs="*"
        )
        self.parser.add_argument("--iso", choices=PromptService.isos())
        self.parser.add_argument(
            "--resolution", choices=PromptService.resolutions(), nargs="*"
        )
        self.parser.add_argument(
            "--compel_style", choices=PromptService.compel_styles()
        )
        self.parser.add_argument("-o", "--output", help="The txt file to generate")

    def execute(self, args):
        if not sys.stdin.isatty():
            args.description = sys.stdin.read().strip().splitlines() + args.description
        _logger.info('Creating prompt for "{0}"'.format(args.description))
        result = PromptService().generate(**vars(args))

        if args.output != None:
            os.makedirs(os.path.dirname(args.output), exist_ok=True)
            f = open(args.output, "w")
            f.write(result)
            f.close()
        else:
            print(result)
