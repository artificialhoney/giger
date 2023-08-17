import argparse
import io
import os
import random
from unittest.mock import MagicMock

import yaml

from giger.commands.image import ImageCommand
from giger.services.image import ImageService

__author__ = "Sebastian Krüger"
__copyright__ = "Sebastian Krüger"
__license__ = "MIT"


def test_execute_txt2img(snapshot, monkeypatch):
    """ImageCommand().txt2img"""
    snapshots_dir = os.path.join(
        os.path.dirname(__file__), "..", "snapshots", "commands", "image", "txt2img"
    )
    snapshot.snapshot_dir = snapshots_dir

    fixtures = [
        (
            "basic",
            {
                "prompt": ["and a beautiful wife"],
                "seed": 0,
                "batch_count": 1,
                "batch_size": 1,
                "output": "images",
                "width": 512,
                "height": 512,
                "lora_model": ["lora_model"],
                "lora_filename": ["lora_filename"],
                "lora_scale": [1.0],
                "name": "viking",
                "input": None,
                "model": "test",
                "negative_prompt": None,
                "inference_steps": 30,
            },
            "A viking with long hair and sword",
        )
    ]
    parser = argparse.ArgumentParser().add_subparsers()
    txt2img = ImageService.txt2img
    ImageService.txt2img = MagicMock()
    random.randint = MagicMock()
    random.randint.return_value = 0
    for test_name, fixture, stdin in fixtures:
        if stdin:
            monkeypatch.setattr("sys.stdin", io.StringIO(stdin))

        ImageCommand(parser).execute(argparse.Namespace(**fixture))

        snapshot.assert_match(
            yaml.dump(ImageService.txt2img.call_args.args),
            os.path.join(snapshots_dir, test_name + ".yml.snapshot"),
        )

    ImageService.txt2img = txt2img


def test_execute_img2img(snapshot):
    """ImageCommand().img2img"""
    snapshots_dir = os.path.join(
        os.path.dirname(__file__), "..", "snapshots", "commands", "image", "img2img"
    )
    snapshot.snapshot_dir = snapshots_dir

    fixtures = [
        (
            "basic",
            {
                "prompt": ["A viking with long hair and sword"],
                "seed": None,
                "batch_count": 1,
                "batch_size": 1,
                "output": "images",
                "width": 512,
                "height": 512,
                "lora_model": [],
                "name": "viking",
                "input": "image.png",
                "model": "test",
                "negative_prompt": None,
                "inference_steps": 30,
                "controlnet_model": None,
            },
        )
    ]
    parser = argparse.ArgumentParser().add_subparsers()
    img2img = ImageService.img2img
    ImageService.img2img = MagicMock()
    random.randint = MagicMock()
    random.randint.return_value = 0
    for test_name, fixture in fixtures:
        ImageCommand(parser).execute(argparse.Namespace(**fixture))

        snapshot.assert_match(
            yaml.dump(ImageService.img2img.call_args.args),
            os.path.join(snapshots_dir, test_name + ".yml.snapshot"),
        )

    ImageService.img2img = img2img


def test_execute_controlnet(snapshot):
    """ImageCommand().controlnet"""
    snapshots_dir = os.path.join(
        os.path.dirname(__file__), "..", "snapshots", "commands", "image", "controlnet"
    )
    snapshot.snapshot_dir = snapshots_dir

    fixtures = [
        (
            "basic",
            {
                "prompt": ["A viking with long hair and sword"],
                "seed": None,
                "batch_count": 1,
                "batch_size": 1,
                "output": "images",
                "width": 512,
                "height": 512,
                "lora_model": [],
                "name": "viking",
                "input": "image.png",
                "model": "test",
                "negative_prompt": None,
                "inference_steps": 30,
                "controlnet_model": "controlnet",
                "controlnet_conditioning_scale": 1.0,
                "control_guidance_start": 1.0,
                "control_guidance_end": 1.0,
            },
        )
    ]
    parser = argparse.ArgumentParser().add_subparsers()
    controlnet = ImageService.controlnet
    ImageService.controlnet = MagicMock()
    random.randint = MagicMock()
    random.randint.return_value = 0
    for test_name, fixture in fixtures:
        ImageCommand(parser).execute(argparse.Namespace(**fixture))

        snapshot.assert_match(
            yaml.dump(ImageService.controlnet.call_args.args),
            os.path.join(snapshots_dir, test_name + ".yml.snapshot"),
        )

    ImageService.controlnet = controlnet
