import argparse
import io
import os
from unittest.mock import MagicMock

import pytest
import yaml

from giger.commands.template import TemplateCommand
from giger.services.template import TemplateService

__author__ = "Sebastian Krüger"
__copyright__ = "Sebastian Krüger"
__license__ = "MIT"


def test_execute(capsys, snapshot, monkeypatch):
    """TemplateCommand().execute"""
    snapshots_dir = os.path.join(
        os.path.dirname(__file__), "..", "snapshots", "commands", "template"
    )
    snapshot.snapshot_dir = snapshots_dir
    output = os.path.join(os.path.dirname(__file__), "..", "tmp", "hero.txt")

    fixtures = [
        (
            "basic",
            {
                "config": ["hero=viking"],
                "data": os.path.join(
                    os.path.dirname(__file__), "..", "fixtures", "hero.yml"
                ),
                "template": ["A {{hero}} with long hair and sword"],
                "output": None,
            },
            None,
        ),
        (
            "data",
            {
                "config": None,
                "data": None,
                "template": ["A {{hero}} with long hair and sword"],
                "output": None,
            },
            None,
        ),
        (
            "output",
            {
                "config": None,
                "data": None,
                "template": ["A {{hero}} with long hair and sword"],
                "output": output,
            },
            None,
        ),
        (
            "stdin",
            {
                "config": None,
                "data": None,
                "template": ["and a beautiful wife"],
                "output": None,
            },
            "A {{hero}} with long hair and sword",
        ),
    ]
    parser = argparse.ArgumentParser().add_subparsers()
    render = TemplateService.render
    TemplateService.render = MagicMock()

    for test_name, fixture, stdin in fixtures:
        TemplateService.render.return_value = test_name

        if stdin:
            monkeypatch.setattr("sys.stdin", io.StringIO(stdin))

        TemplateCommand(parser).execute(argparse.Namespace(**fixture))

        snapshot.assert_match(
            yaml.dump(TemplateService.render.call_args.args),
            os.path.join(snapshots_dir, test_name + ".yml.snapshot"),
        )

        if fixture["output"] != None:
            assert open(output).read() == test_name
        else:
            out, _err = capsys.readouterr()
            assert out.strip() == test_name

    TemplateService.render = render
