import os
from pathlib import Path

from giger.services.roop import RoopService

__author__ = "Sebastian Krüger"
__copyright__ = "Sebastian Krüger"
__license__ = "MIT"


def test_swap():
    """RoopService().swap"""
    tmp_dir = os.path.join(os.path.dirname(__file__), "..", "tmp", "roop")
    os.makedirs(tmp_dir, exist_ok=True)
    face = os.path.join(os.path.dirname(__file__), "..", "fixtures", "face.jpg")
    input = os.path.join(os.path.dirname(__file__), "..", "fixtures", "input.jpg")
    fail = os.path.join(os.path.dirname(__file__), "..", "fixtures", "fail.jpg")
    output = os.path.join(tmp_dir, "output.jpg")
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
