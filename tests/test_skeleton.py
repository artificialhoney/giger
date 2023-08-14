import pytest

from giger.commands import PromptCommand
from giger.skeleton import main

__author__ = "Sebastian Krüger"
__copyright__ = "Sebastian Krüger"
__license__ = "MIT"


def test_prompt(mocker):
    """Prompt Tests"""
    spy = mocker.spy(PromptCommand, "run")
    main(["prompt", '"Spawn in a battle"'])
    spy.assert_called_once_with(21)
