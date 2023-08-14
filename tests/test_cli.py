import os
from unittest.mock import MagicMock

import pytest
import yaml

from giger.cli import CLI
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
                "type=Viking",
                "--data",
                "data/hero.yaml",
                "This is a {{type}}",
            ],
        )
    ]
    for test_name, fixture in fixtures:
        TemplateCommand.run = MagicMock()
        CLI().run(["template"] + fixture)

        snapshot.assert_match(
            yaml.dump(TemplateCommand.run.call_args.args),
            os.path.join(snapshots_dir, test_name + ".yml.snapshot"),
        )


def test_prompt(snapshot):
    """CLI Prompt Tests"""
    snapshots_dir = os.path.join(
        os.path.dirname(__file__), "snapshots", "cli", "prompt"
    )
    snapshot.snapshot_dir = snapshots_dir

    fixtures = [
        ("basic", ["Spawn in a battle", "--time Ancient", "--type", "Comic Book"])
    ]
    for test_name, fixture in fixtures:
        PromptCommand.run = MagicMock()
        CLI().run(["prompt"] + fixture)

        snapshot.assert_match(
            yaml.dump(PromptCommand.run.call_args.args),
            os.path.join(snapshots_dir, test_name + ".yml.snapshot"),
        )


def test_image(snapshot):
    """CLI Image Tests"""
    snapshots_dir = os.path.join(os.path.dirname(__file__), "snapshots", "cli", "image")
    snapshot.snapshot_dir = snapshots_dir

    fixtures = [("basic", ["--output", "out", "--name", "graffiti"])]
    for test_name, fixture in fixtures:
        ImageCommand.run = MagicMock()
        CLI().run(["image"] + fixture)

        snapshot.assert_match(
            yaml.dump(ImageCommand.run.call_args.args),
            os.path.join(snapshots_dir, test_name + ".yml.snapshot"),
        )


def test_roop(snapshot):
    """CLI Roop Tests"""
    snapshots_dir = os.path.join(os.path.dirname(__file__), "snapshots", "cli", "roop")
    snapshot.snapshot_dir = snapshots_dir

    fixtures = [
        (
            "basic",
            ["--source", "face.jpg", "--input", "target.png", "--output", "output.png"],
        )
    ]
    for test_name, fixture in fixtures:
        RoopCommand.run = MagicMock()
        CLI().run(["roop"] + fixture)

        snapshot.assert_match(
            yaml.dump(RoopCommand.run.call_args.args),
            os.path.join(snapshots_dir, test_name + ".yml.snapshot"),
        )
