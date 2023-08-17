import os
from unittest.mock import MagicMock

import yaml
from compel import Compel
from diffusers import (
    ControlNetModel,
    StableDiffusionControlNetPipeline,
    StableDiffusionImg2ImgPipeline,
    StableDiffusionPipeline,
    UniPCMultistepScheduler,
)
from PIL import Image

from giger.services.image import ImageService

__author__ = "Sebastian Krüger"
__copyright__ = "Sebastian Krüger"
__license__ = "MIT"


def test_txt2img(snapshot, monkeypatch):
    """ImageService().txt2img"""
    snapshots_dir = os.path.join(
        os.path.dirname(__file__), "..", "snapshots", "services", "image", "txt2img"
    )
    snapshot.snapshot_dir = snapshots_dir
    tmp_dir = os.path.join(os.path.dirname(__file__), "..", "tmp", "image", "txt2img")
    os.makedirs(tmp_dir, exist_ok=True)
    input = os.path.join(os.path.dirname(__file__), "..", "fixtures", "input.jpg")
    fixtures = [
        (
            "basic",
            {
                "model": "test",
                "prompt": "A viking with long hair and sword",
                "negative_prompt": None,
                "output": tmp_dir,
                "width": 512,
                "height": 512,
                "loras": [{"model": "model", "filename": "filename", "scale": 1.0}],
            },
            True,
        )
    ]

    from_pretrained = StableDiffusionPipeline.from_pretrained
    StableDiffusionPipeline.from_pretrained = MagicMock()
    pipeline_mock = MagicMock()
    pipeline_mock.to = MagicMock()
    pipeline_mock.enable_model_cpu_offload = MagicMock()
    pipeline_mock.enable_xformers_memory_efficient_attention = MagicMock()
    pipeline_mock.load_lora_weights = MagicMock()
    pipeline_mock.return_value = [[Image.open(input)]]
    StableDiffusionPipeline.from_pretrained.return_value = pipeline_mock
    Compel.build_conditioning_tensor = MagicMock()
    from giger.services.image import ImageService

    for test_name, fixture, cuda in fixtures:

        def is_available():
            return cuda

        monkeypatch.setattr("torch.cuda.is_available", is_available)
        ImageService().txt2img(*fixture.values())
        snapshot.assert_match(
            yaml.dump(StableDiffusionPipeline.from_pretrained.call_args.args),
            os.path.join(snapshots_dir, test_name + ".from_pretrained.yml.snapshot"),
        )
        snapshot.assert_match(
            yaml.dump(pipeline_mock.call_args.args),
            os.path.join(snapshots_dir, test_name + ".pipeline.yml.snapshot"),
        )

    StableDiffusionPipeline.from_pretrained = from_pretrained


def test_img2img(snapshot, monkeypatch):
    """ImageService().img2img"""
    snapshots_dir = os.path.join(
        os.path.dirname(__file__), "..", "snapshots", "services", "image", "img2img"
    )
    snapshot.snapshot_dir = snapshots_dir
    tmp_dir = os.path.join(os.path.dirname(__file__), "..", "tmp", "image", "img2img")
    os.makedirs(tmp_dir, exist_ok=True)
    input = os.path.join(os.path.dirname(__file__), "..", "fixtures", "input.jpg")
    fixtures = [
        (
            "basic",
            {
                "model": "test",
                "prompt": "A viking with long hair and sword",
                "negative_prompt": None,
                "output": tmp_dir,
                "width": 512,
                "height": 512,
                "input": input,
            },
            False,
        )
    ]

    from_pretrained = StableDiffusionImg2ImgPipeline.from_pretrained
    StableDiffusionImg2ImgPipeline.from_pretrained = MagicMock()
    pipeline_mock = MagicMock()
    pipeline_mock.to = MagicMock()
    pipeline_mock.enable_model_cpu_offload = MagicMock()
    pipeline_mock.enable_xformers_memory_efficient_attention = MagicMock()
    pipeline_mock.load_lora_weights = MagicMock()
    pipeline_mock.return_value = [[Image.open(input)]]
    StableDiffusionImg2ImgPipeline.from_pretrained.return_value = pipeline_mock
    Compel.build_conditioning_tensor = MagicMock()
    from giger.services.image import ImageService

    for test_name, fixture, cuda in fixtures:

        def is_available():
            return cuda

        monkeypatch.setattr("torch.cuda.is_available", is_available)
        ImageService().img2img(*fixture.values())
        snapshot.assert_match(
            yaml.dump(StableDiffusionImg2ImgPipeline.from_pretrained.call_args.args),
            os.path.join(snapshots_dir, test_name + ".from_pretrained.yml.snapshot"),
        )
        snapshot.assert_match(
            yaml.dump(pipeline_mock.call_args.args),
            os.path.join(snapshots_dir, test_name + ".pipeline.yml.snapshot"),
        )

    StableDiffusionImg2ImgPipeline.from_pretrained = from_pretrained


def test_controlnet(snapshot, monkeypatch):
    """ImageService().controlnet"""
    snapshots_dir = os.path.join(
        os.path.dirname(__file__), "..", "snapshots", "services", "image", "controlnet"
    )
    snapshot.snapshot_dir = snapshots_dir
    tmp_dir = os.path.join(
        os.path.dirname(__file__), "..", "tmp", "image", "controlnet"
    )
    os.makedirs(tmp_dir, exist_ok=True)
    input = os.path.join(os.path.dirname(__file__), "..", "fixtures", "input.jpg")
    data = {
        "model": "test",
        "prompt": "A viking with long hair and sword",
        "negative_prompt": None,
        "output": tmp_dir,
        "width": 512,
        "height": 512,
        "controlnet_model": "test",
        "controlnet_conditioning_scale": 1,
        "control_guidance_start": 1,
        "control_guidance_end": 1,
        "input": input,
    }

    fixtures = [("basic", data, False), ("cuda", data, True)]

    from_pretrained = StableDiffusionControlNetPipeline.from_pretrained
    StableDiffusionControlNetPipeline.from_pretrained = MagicMock()
    pipeline_mock = MagicMock()
    pipeline_mock.to = MagicMock()
    pipeline_mock.enable_model_cpu_offload = MagicMock()
    pipeline_mock.enable_xformers_memory_efficient_attention = MagicMock()
    pipeline_mock.load_lora_weights = MagicMock()
    pipeline_mock.return_value = [[Image.open(input)]]
    StableDiffusionControlNetPipeline.from_pretrained.return_value = pipeline_mock
    Compel.build_conditioning_tensor = MagicMock()
    UniPCMultistepScheduler.from_config = MagicMock()
    ControlNetModel.from_pretrained = MagicMock()
    from giger.services.image import ImageService

    for test_name, fixture, cuda in fixtures:

        def is_available():
            return cuda

        monkeypatch.setattr("torch.cuda.is_available", is_available)
        ImageService().controlnet(*fixture.values())
        snapshot.assert_match(
            yaml.dump(StableDiffusionControlNetPipeline.from_pretrained.call_args.args),
            os.path.join(snapshots_dir, test_name + ".from_pretrained.yml.snapshot"),
        )
        snapshot.assert_match(
            yaml.dump(pipeline_mock.call_args.args),
            os.path.join(snapshots_dir, test_name + ".pipeline.yml.snapshot"),
        )

    StableDiffusionControlNetPipeline.from_pretrained = from_pretrained
