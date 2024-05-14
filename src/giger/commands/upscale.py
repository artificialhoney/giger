import logging
import os
import sys

import yaml

_logger = logging.getLogger(__name__)


class UpscaleCommand:
    def __init__(self, parser):
        self.parser = parser.add_parser("upscale", help="Upscale image")
        self.parser.add_argument("-i", "--input", help="The input image", required=True)
        self.parser.add_argument(
            "-o", "--output", help="The output image folder", required=True
        )

    def execute(self, args):
        _logger.info(
            'Upscaling image with input from "{0}" to "{1}"'.format(
                args.input, args.output
            )
        )
        from ..services.upscale import UpscaleService

        UpscaleService().upscale(args.input, args.output)
