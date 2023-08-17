import hashlib
import os
from pathlib import Path
from unittest.mock import MagicMock

from giger.services.roop import RoopService

__author__ = "Sebastian Krüger"
__copyright__ = "Sebastian Krüger"
__license__ = "MIT"


def test_swap(snapshot):
    """RoopService().swap"""
    snapshots_dir = os.path.join(
        os.path.dirname(__file__), "..", "snapshots", "services", "roop"
    )
    tmp_dir = os.path.join(os.path.dirname(__file__), "..", "tmp", "roop")
    os.makedirs(tmp_dir, exist_ok=True)
    face = os.path.join(os.path.dirname(__file__), "..", "fixtures", "face.jpg")
    input = os.path.join(os.path.dirname(__file__), "..", "fixtures", "input.jpg")
    fail = os.path.join(os.path.dirname(__file__), "..", "fixtures", "fail.jpg")
    output = os.path.join(tmp_dir, "output.jpg")
    snapshot.snapshot_dir = snapshots_dir
    fixtures = [
        ("basic", face, input, os.path.join(tmp_dir, "basic.jpg"), None),
        ("fail", face, fail, os.path.join(tmp_dir, "fail.jpg"), None),
        ("fail", fail, input, os.path.join(tmp_dir, "fail.jpg"), None),
        (
            "fail",
            face,
            input,
            os.path.join(tmp_dir, "fail.jpg"),
            os.path.join(Path.home(), "roop", "GFPGANv1.4.pth"),
        ),
    ]

    for test_name, face, input, output, model_name in fixtures:
        RoopService().swap(face, input, output, model_name=model_name)
        assert os.path.exists(output) == (test_name != "fail")
        if os.path.exists(output):
            snapshot.assert_match(
                hashlib.sha1(
                    open(
                        output,
                        "rb",
                    ).read()
                ).hexdigest(),
                os.path.join(snapshots_dir, test_name + ".jpg.snapshot"),
            )
