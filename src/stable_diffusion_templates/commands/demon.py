import yaml
import logging

_logger = logging.getLogger(__name__)

from ..services.demon import DemonService

class DemonCommand: 
    def __init__(self, parser):
        self.parser = parser.add_parser("demon", help="Demon batch prompts")
        self.parser.add_argument("-t", "--template", help="The prompt template", required=True)
        self.parser.add_argument("-i", "--input", help="The text file", required=True)
        self.parser.add_argument("-d", "--data", help="The prompt data", required=True)
        self.parser.add_argument("-o", "--output", help="The output directory to generate image in", required=True)
        self.parser.add_argument("-m",
                              "--model", help="The Stable Diffusion model to use", default="Lykon/DreamShaper")
        self.parser.add_argument("-a",
                              "--alias", help="The model alias to use", default="dreamshaper")

        self.parser.add_argument("-n", "--name", help="Name of the text", required=True)
        self.parser.add_argument("-p",
                              "--part", help="Part of input", required=True)
    def run(self, args):
        self.service = DemonService(args.model, args.alias)
        f = open(args.template, "r")
        template = f.read()
        f.close()

        f = open(args.input, "r")
        input = f.read()
        f.close()

        f = open(args.data, "r")
        data = yaml.safe_load(f)
        f.close()

        _logger.info("Running demon batch for '{0}'".format(args.name))

        data["name"] = args.name
        self.service.render(args.name, args.part, input, args.output, template, data)
            
