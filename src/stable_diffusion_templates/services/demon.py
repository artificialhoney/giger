import os
import pathlib

from .template import TemplateService
from .image import ImageService 

class DemonService:
    def __init__(self, model, alias):
        self.template_service = TemplateService()
        self.image_service = ImageService(model)
        self.amodel_alias = alias
    def render(self, title, part, text, out, template, data):
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

        image_name = self.model_alias

        for i, val in enumerate(prompts):
            pathlib.Path(os.path.join(out, title, part)).mkdir(parents=True, exist_ok=True)
            path = os.path.join(out, title, part, str(
                i).rjust(3, "0") + "_" + image_name + ".demon.png")
            data["text"] = val
            p = self.template_service.render(template, data)

            width = 768
            height = 432

            self.image_service.txt2img(p, path.replace("demon", "demon.wide"), width, height)
            self.image_service.txt2img(p, path.replace("demon", "demon.wide"), height, width)