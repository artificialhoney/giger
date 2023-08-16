import os

from giger.services.prompt import PromptService

__author__ = "Sebastian Krüger"
__copyright__ = "Sebastian Krüger"
__license__ = "MIT"


def test_generate(snapshot):
    """PromptService().generate"""
    snapshots_dir = os.path.join(
        os.path.dirname(__file__), "..", "snapshots", "services", "prompt"
    )
    snapshot.snapshot_dir = snapshots_dir
    data = {
        "time": "Time",
        "type": "Type",
        "background_color": "BackgroundColor",
        "art_style": ["ArtStyle"],
        "artist": ["Artist"],
        "realism": ["Realism"],
        "rendering_engine": ["RenderingEngine"],
        "lightning_angle": ["LightningAngle"],
        "lightning_style": ["LightningStyle"],
        "camera_position": ["CameraPosition"],
        "camera": ["Camera"],
        "composition": ["Composition"],
        "iso": "Iso",
        "resolution": ["Resolution"],
    }
    fixtures = [
        (
            "basic",
            {
                "description": ["A viking with long hair and sword"],
            },
        ),
        ("advanced", data | {"description": ["A viking with long hair and sword"]}),
        (
            "compel_subtle",
            data
            | {
                "description": ["A viking with long hair and sword"],
                "compel_style": "subtle",
            },
        ),
        (
            "compel_full",
            data
            | {
                "description": ["A viking with long hair and sword"],
                "compel_style": "full",
            },
        ),
        ("compel_subtle_empty", {"compel_style": "subtle"}),
        ("compel_full_full", {"compel_style": "full"}),
    ]

    for test_name, fixture in fixtures:
        snapshot.assert_match(
            PromptService().generate(**fixture),
            os.path.join(snapshots_dir, test_name + ".txt.snapshot"),
        )
