import pytest

from giger.cli import CLI
from giger.commands.prompt import PromptCommand

__author__ = "Sebastian Krüger"
__copyright__ = "Sebastian Krüger"
__license__ = "MIT"


def test_prompt(mocker):
    """Prompt Tests"""
    spy = mocker.spy(PromptCommand, "run")
    CLI().run(["prompt", '"Spawn in a battle"'])
    spy.assert_called_once()
