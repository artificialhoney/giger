import argparse
import io
import os
from unittest.mock import DEFAULT, MagicMock

import yaml

from giger.commands.prompt import PromptCommand
from giger.services.prompt import PromptService

__author__ = "Sebastian Krüger"
__copyright__ = "Sebastian Krüger"
__license__ = "MIT"


def test_execute(capsys, snapshot, monkeypatch):
    """PromptCommand().execute"""
    snapshots_dir = os.path.join(
        os.path.dirname(__file__), "..", "snapshots", "commands", "prompt"
    )
    snapshot.snapshot_dir = snapshots_dir
    output = os.path.join(os.path.dirname(__file__), "..", "tmp", "hero.txt")

    fixtures = [
        (
            "basic",
            {"description": ["A viking with long hair and sword"], "output": None},
            None,
        ),
        (
            "output",
            {"description": ["A viking with long hair and sword"], "output": output},
            None,
        ),
        (
            "stdin",
            {"description": ["and a beautiful wife"], "output": None},
            "A viking with long hair and sword",
        ),
    ]
    parser = argparse.ArgumentParser().add_subparsers()
    generate = PromptService.generate
    PromptService.generate = MagicMock()

    for test_name, fixture, stdin in fixtures:
        PromptService.generate.return_value = test_name

        if stdin:
            monkeypatch.setattr("sys.stdin", io.StringIO(stdin))

        PromptCommand(parser).execute(argparse.Namespace(**fixture))

        snapshot.assert_match(
            yaml.dump(PromptService.generate.call_args.args),
            os.path.join(snapshots_dir, test_name + ".yml.snapshot"),
        )

        if fixture["output"] != None:
            assert open(output).read() == test_name
        else:
            out, _err = capsys.readouterr()
            assert out.strip() == test_name

    PromptService.generate = generate
