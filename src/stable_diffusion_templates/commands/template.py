import yaml
import logging

_logger = logging.getLogger(__name__)

from ..services.template import TemplateService 


class TemplateCommand:
    def __init__(self, parser):
        self.parser = parser.add_parser("template", help="Template prompts")
        self.parser.add_argument("-t", "--template", help="The prompt template", required=True)
        self.parser.add_argument("-d", "--data", help="The prompt data", required=True)
        self.parser.add_argument("-o", "--out", help="The txt file to generate")
        self.service = TemplateService()
    def run(self, args):
        f = open(args.template, "r")
        template = f.read()
        f.close()

        f = open(args.data, "r")
        data = yaml.safe_load(f)
        f.close()

        _logger.info("Running template with input from {0} and data {1}".format(args.template, data))

        result = self.service.render(template, data)

        if args.out:
            f = open(args.out, "w")
            f.write(result)
            f.close()
        else:
            print(result)
