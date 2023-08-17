#!/usr/bin/env python

import argparse
import logging
import sys
import warnings

from diffusers import utils

from giger import __version__

from .commands.image import ImageCommand
from .commands.prompt import PromptCommand
from .commands.roop import RoopCommand
from .commands.template import TemplateCommand

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

        self.template = TemplateCommand(subparsers)
        self.prompt = PromptCommand(subparsers)
        self.image = ImageCommand(subparsers)
        self.roop = RoopCommand(subparsers)

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

        if loglevel == logging.DEBUG:
            utils.logging.set_verbosity_debug()
        elif loglevel == logging.INFO:
            utils.logging.set_verbosity_info()
        else:
            utils.logging.set_verbosity_error()

    def run(self, args):
        args = self.parse_args(args)
        self.setup_logging(args.loglevel)
        if args.command == "template":
            self.template.execute(args)
        elif args.command == "prompt":
            self.prompt.execute(args)
        elif args.command == "image":
            self.image.execute(args)
        else:
            self.roop.execute(args)


def run():
    CLI().run(sys.argv[1:])


if __name__ == "__main__":
    run()
