#!/usr/bin/env python

import argparse
import logging
import sys
import warnings

from giger import __version__

from .commands.image import ImageCommand
from .commands.prompt import PromptCommand
from .commands.swap import SwapCommand
from .commands.upscale import UpscaleCommand

warnings.filterwarnings("ignore", category=FutureWarning)


__author__ = "Sebastian Krüger"
__copyright__ = "Sebastian Krüger"
__license__ = "MIT"


# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


class CLI:
    def parse_args(self, args):
        """
        Parse command line parameters
        """

        parser = argparse.ArgumentParser(
            prog="giger", description="Tools for Stable Diffusion"
        )

        parser.add_argument(
            "--version",
            action="version",
            version=f"giger {__version__}",
        )
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

        subparsers = parser.add_subparsers(dest="command", required=True)

        self.prompt = PromptCommand(subparsers)
        self.image = ImageCommand(subparsers)
        self.swap = SwapCommand(subparsers)
        self.upscale = UpscaleCommand(subparsers)

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
        args = self.parse_args(args)
        self.setup_logging(args.loglevel)
        if args.command == "prompt":
            self.prompt.execute(args)
        elif args.command == "image":
            from diffusers import utils

            if args.loglevel == logging.DEBUG:
                utils.logging.set_verbosity_debug()
            elif args.loglevel == logging.INFO:
                utils.logging.set_verbosity_info()
            else:
                utils.logging.set_verbosity_error()
            self.image.execute(args)
        elif args.command == "upscale":
            self.upscale.execute(args)
        else:
            self.swap.execute(args)


def run():
    CLI().run(sys.argv[1:])


if __name__ == "__main__":
    run()
