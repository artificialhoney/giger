import os
from unittest.mock import MagicMock

import pytest
import yaml

from giger.cli import CLI
from giger.commands.prompt import PromptCommand

__author__ = "Sebastian Krüger"
__copyright__ = "Sebastian Krüger"
__license__ = "MIT"


def test_prompt(snapshot):
    """CLI Prompt Tests"""
    snapshots_dir = os.path.join(os.path.dirname(__file__), "snapshots", "cli")
    snapshot.snapshot_dir = snapshots_dir

    fixtures = [("basic", ["This is a test"])]
    for test_name, fixture in fixtures:
        PromptCommand.run = MagicMock()
        CLI().run(["prompt"] + fixture)

        snapshot.assert_match(
            yaml.dump(PromptCommand.run.call_args.args),
            os.path.join(snapshots_dir, test_name + ".yml.snapshot"),
        )
