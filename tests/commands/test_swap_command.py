import argparse
import os
from unittest.mock import MagicMock

import yaml

from giger.commands.swap import SwapCommand
from giger.services.swap import SwapService

__author__ = "Sebastian Krüger"
__copyright__ = "Sebastian Krüger"
__license__ = "MIT"


def test_execute(snapshot):
    """SwapCommand().execute"""
    snapshots_dir = os.path.join(
        os.path.dirname(__file__), "..", "snapshots", "commands", "swap"
    )
    snapshot.snapshot_dir = snapshots_dir

    parser = argparse.ArgumentParser().add_subparsers()
    swap = SwapService.swap
    SwapService.swap = MagicMock()
    SwapCommand(parser).execute(
        argparse.Namespace(
            face="face.png", input="input.png", output="output.png", model=None
        )
    )

    snapshot.assert_match(
        yaml.dump(SwapService.swap.call_args.args),
        os.path.join(snapshots_dir, "basic.yml.snapshot"),
    )

    SwapService.swap = swap
