from ..services.template import TemplateService
import yaml
import logging
import sys
import io

_logger = logging.getLogger(__name__)


class TemplateCommand:
    def __init__(self, parser):
        self.parser = parser.add_parser("template", help="Template prompts")
        self.parser.add_argument("template", help="The prompt template", nargs="?", default=(
            None if sys.stdin.isatty() else sys.stdin))
        self.parser.add_argument(
            "-c", "--config", help="The prompt data in the format 'key=value'", nargs="*")
        self.parser.add_argument("-d", "--data", help="The prompt data")
        self.parser.add_argument("-o", "--out", help="The txt file to generate")
        self.service = TemplateService()

    def run(self, args):
        if args.data != None:
            f = open(args.data, "r")
            data = yaml.safe_load(f)
            f.close()
        else:
            data = {}

        if args.config != None:
            for c in args.config:
                split = c.split("=")
                data[split[0]] = split[1]

        _logger.info("Running template with input from {0} and data {1}".format(
            args.template, data))

        if isinstance(args.template, io.TextIOWrapper):
            template = args.template.read()
        else:
            template = args.template

        result = self.service.render(template, data)

        if args.out:
            f = open(args.out, "w")
            f.write(result)
            f.close()
        else:
            print(result)
