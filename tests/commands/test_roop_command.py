import argparse
import os
from unittest.mock import DEFAULT, MagicMock

import yaml

from giger.commands.roop import RoopCommand
from giger.services.roop import RoopService

__author__ = "Sebastian Krüger"
__copyright__ = "Sebastian Krüger"
__license__ = "MIT"


def test_execute(snapshot):
    """RoopCommand().execute"""
    snapshots_dir = os.path.join(
        os.path.dirname(__file__), "..", "snapshots", "commands", "roop"
    )
    snapshot.snapshot_dir = snapshots_dir

    parser = argparse.ArgumentParser().add_subparsers()
    swap = RoopService.swap
    RoopService.swap = MagicMock()
    RoopCommand(parser).execute(
        argparse.Namespace(
            face="face.png", input="input.png", output="output.png", model=None
        )
    )

    snapshot.assert_match(
        yaml.dump(RoopService.swap.call_args.args),
        os.path.join(snapshots_dir, "basic.yml.snapshot"),
    )

    RoopService.swap = swap
