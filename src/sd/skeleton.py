#!/usr/bin/env python

"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         fibonacci = stable_diffusion_templates.skeleton:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This file can be renamed depending on your needs or safely removed if not needed.

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import argparse
import logging
import sys

from sd import __version__

from .commands.template import TemplateCommand
from .commands.prompt import PromptCommand
from .commands.image import ImageCommand
from .commands.roop import RoopCommand

__author__ = "Sebastian Krüger"
__copyright__ = "Sebastian Krüger"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.

class CLI():
    def parse_args(self, args):
        """Parse command line parameters

        Args:
        args (List[str]): command line parameters as list of strings
            (for example  ``["--help"]``).

        Returns:
        :obj:`argparse.Namespace`: command line parameters namespace
        """
        parser = argparse.ArgumentParser(
            prog="sd", description="Tools for Stable Diffusion")

        parser.add_argument(
            "--version",
            action="version",
            version=f"sd {__version__}",
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
        """Setup basic logging

        Args:
        loglevel (int): minimum loglevel for emitting messages
        """
        logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
        logging.basicConfig(
            level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
        )

    def run(self, args):
        """Wrapper allowing :func:`fib` to be called with string arguments in a CLI fashion

        Instead of returning the value from :func:`fib`, it prints the result to the
        ``stdout`` in a nicely formatted message.

        Args:
        args (List[str]): command line parameters as list of strings
            (for example  ``["--verbose", "42"]``).
        """
        args = self.parse_args(args)
        self.setup_logging(args.loglevel)
        if args.command == 'template':
            self.template.run(args)
        elif args.command == 'prompt':
            self.prompt.run(args)
        elif args.command == 'image':
            self.image.run(args)
        elif args.command == 'roop':
            self.roop.run(args)

def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with setuptools.
    """
    CLI().run(sys.argv[1:])


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m stable_diffusion_templates.skeleton 42
    #
    run()
