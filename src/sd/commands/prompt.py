import logging
import sys

_logger = logging.getLogger(__name__)

from ..services.prompt import PromptService

class PromptCommand: 
    def __init__(self, parser):
        self.service = PromptService()
        self.parser = parser.add_parser("prompt", help="Generate prompt")
        self.parser.add_argument("description", nargs="?", default=(None if sys.stdin.isatty() else sys.stdin))
        self.parser.add_argument("--time", choices=self.service.times())
        self.parser.add_argument("--type", choices=self.service.types())
        self.parser.add_argument("--background_color")
        self.parser.add_argument("--art_style", choices=self.service.art_styles(), nargs="*")
        self.parser.add_argument("--artist", choices=self.service.artists(), nargs="*")
        self.parser.add_argument("--realism", choices=self.service.realisms(), nargs="*")
        self.parser.add_argument("--rendering_engine", choices=self.service.rendering_engines(), nargs="*")
        self.parser.add_argument("--lightning_angle", choices=self.service.lightning_angles(), nargs="*")
        self.parser.add_argument("--lightning_style", choices=self.service.lightning_styles(), nargs="*")
        self.parser.add_argument("--camera_position", choices=self.service.camera_positions(), nargs="*")
        self.parser.add_argument("--camera", choices=self.service.cameras(), nargs="*")
        self.parser.add_argument("--style", choices=self.service.styles(), nargs="*")
        self.parser.add_argument("--composition", choices=self.service.compositions(), nargs="*")
        self.parser.add_argument("--iso", choices=self.service.isos())
        self.parser.add_argument("--resolution", choices=self.service.resolutions(), nargs="*")
        self.parser.add_argument("--compel", default=False, type=bool)

    def run(self, args):
        _logger.info("Creating prompt for '{0}'".format(args.description))
        print(self.service.generate(args))