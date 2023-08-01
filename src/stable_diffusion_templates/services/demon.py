from diffusers import DiffusionPipeline
import torch
import os
import piexif
import pathlib

from .template import TemplateService 

class DemonService:
    def __init__(self):
        self.service = TemplateService()
    def render(self, title, model, alias, part, text, out, template, data):
        pipeline = DiffusionPipeline.from_pretrained(
                model, torch_dtype=torch.float32)

        lines = []
        f = text.split("\n")
        start = None
        for i, row in enumerate(f):
            if i == 0:
                continue
            if row.strip() == part:
                start = i
                continue
            if row.strip() == "":
                if start != None:
                    break
                else:
                    continue
            if start:
                lines.append(row.strip())

        prompts = []
        for i, line in enumerate(lines):
            if i % 2 == 1:
                prompts[-1] = prompts[-1] + " " + line
            else:
                prompts.append(line)

        image_name = alias + ".pretrained"

        for i, val in enumerate(prompts):
            pathlib.Path(os.path.join(out, title, part)).mkdir(parents=True, exist_ok=True)
            path = os.path.join(out, title, part, str(
                i).rjust(3, "0") + "_" + image_name + ".demon.png")
            data["text"] = val
            p = self.service.render(template, data)

            exif_ifd = {piexif.ImageIFD.ImageDescription: p.encode()}
            exif_dict = {
                "0th": exif_ifd, "Exif": {}, "1st": {},
                "thumbnail": None, "GPS": {}
            }
            exif_bytes = piexif.dump(exif_dict)

            width = 768
            height = 432

            image = pipeline(p, width=width, height=height).images[0]
            image.save(path.replace("demon", "demon.wide"), exif=exif_bytes)

            image = pipeline(p, width=height, height=width).images[0]
            image.save(path.replace("demon", "demon.narrow"), exif=exif_bytes)