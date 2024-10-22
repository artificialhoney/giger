import os
import sys
from unittest.mock import MagicMock

import pytest
import yaml
from diffusers.utils import logging

from giger.cli import run
from giger.commands.image import ImageCommand
from giger.commands.prompt import PromptCommand
from giger.commands.swap import SwapCommand

__author__ = "Sebastian Krüger"
__copyright__ = "Sebastian Krüger"
__license__ = "MIT"


def test_loglevel():
    """CLI Loglevel Tests"""
    fixtures = [(logging.INFO, "-v"), (logging.DEBUG, "-vv")]
    execute = ImageCommand.execute
    ImageCommand.execute = MagicMock()

    for loglevel, fixture in fixtures:
        sys.argv = [
            "giger",
            fixture,
            "image",
            "A viking with long hair and sword",
            "--output",
            "viking",
        ]
        run()
        assert logging.get_verbosity() == loglevel
    ImageCommand.execute = execute


def test_prompt(snapshot):
    """CLI Prompt Tests"""
    snapshots_dir = os.path.join(
        os.path.dirname(__file__), "snapshots", "cli", "prompt"
    )
    snapshot.snapshot_dir = snapshots_dir

    fixtures = [
        (
            "basic",
            [
                "A viking with long hair and sword",
            ],
        )
    ]
    execute = PromptCommand.execute
    PromptCommand.execute = MagicMock()
    for test_name, fixture in fixtures:
        sys.argv = ["giger", "prompt"] + fixture
        PromptCommand.execute = MagicMock()
        run()

        snapshot.assert_match(
            yaml.dump(PromptCommand.execute.call_args.args),
            os.path.join(snapshots_dir, test_name + ".yml.snapshot"),
        )
    PromptCommand.execute = execute


def test_swap(snapshot):
    """CLI Swap Tests"""
    snapshots_dir = os.path.join(os.path.dirname(__file__), "snapshots", "cli", "swap")
    snapshot.snapshot_dir = snapshots_dir

    fixtures = [
        (
            "basic",
            ["--input", "image.png", "--face", "face.png", "--output", "output.png"],
        )
    ]
    execute = SwapCommand.execute
    SwapCommand.execute = MagicMock()
    for test_name, fixture in fixtures:
        sys.argv = ["giger", "swap"] + fixture
        SwapCommand.execute = MagicMock()
        run()

        snapshot.assert_match(
            yaml.dump(SwapCommand.execute.call_args.args),
            os.path.join(snapshots_dir, test_name + ".yml.snapshot"),
        )
    SwapCommand.execute = execute


def test_image(snapshot):
    """CLI Image Tests"""
    snapshots_dir = os.path.join(os.path.dirname(__file__), "snapshots", "cli", "image")
    snapshot.snapshot_dir = snapshots_dir

    fixtures = [
        (
            "basic",
            ["--output", "output.png"],
        )
    ]
    execute = ImageCommand.execute
    ImageCommand.execute = MagicMock()
    for test_name, fixture in fixtures:
        sys.argv = ["giger", "image"] + fixture
        ImageCommand.execute = MagicMock()
        run()

        snapshot.assert_match(
            yaml.dump(ImageCommand.execute.call_args.args),
            os.path.join(snapshots_dir, test_name + ".yml.snapshot"),
        )
    ImageCommand.execute = execute
