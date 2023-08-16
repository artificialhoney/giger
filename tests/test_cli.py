import os
import sys
from unittest.mock import MagicMock

import pytest
import yaml

from giger.cli import run
from giger.commands.image import ImageCommand
from giger.commands.prompt import PromptCommand
from giger.commands.roop import RoopCommand
from giger.commands.template import TemplateCommand

__author__ = "Sebastian Krüger"
__copyright__ = "Sebastian Krüger"
__license__ = "MIT"


def test_template(snapshot):
    """CLI Template Tests"""
    snapshots_dir = os.path.join(
        os.path.dirname(__file__), "snapshots", "cli", "template"
    )
    snapshot.snapshot_dir = snapshots_dir

    fixtures = [
        (
            "basic",
            [
                "--config",
                "hero=Viking",
                "--data",
                "hero.yml",
                "A {{hero}} with long hair and sword",
            ],
        )
    ]
    execute = TemplateCommand.execute
    TemplateCommand.execute = MagicMock()
    for test_name, fixture in fixtures:
        sys.argv = ["giger", "template"] + fixture
        run()

        snapshot.assert_match(
            yaml.dump(TemplateCommand.execute.call_args.args),
            os.path.join(snapshots_dir, test_name + ".yml.snapshot"),
        )
    TemplateCommand.execute = execute


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


def test_roop(snapshot):
    """CLI Roop Tests"""
    snapshots_dir = os.path.join(os.path.dirname(__file__), "snapshots", "cli", "roop")
    snapshot.snapshot_dir = snapshots_dir

    fixtures = [
        (
            "basic",
            ["--input", "image.png", "--face", "face.png", "--output", "output.png"],
        )
    ]
    execute = RoopCommand.execute
    RoopCommand.execute = MagicMock()
    for test_name, fixture in fixtures:
        sys.argv = ["giger", "roop"] + fixture
        RoopCommand.execute = MagicMock()
        run()

        snapshot.assert_match(
            yaml.dump(RoopCommand.execute.call_args.args),
            os.path.join(snapshots_dir, test_name + ".yml.snapshot"),
        )
    RoopCommand.execute = execute


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
