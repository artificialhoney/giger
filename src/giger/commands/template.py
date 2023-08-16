import logging
import os
import sys

import yaml

_logger = logging.getLogger(__name__)


class TemplateCommand:
    def __init__(self, parser):
        self.parser = parser.add_parser("template", help="Template prompts")
        self.parser.add_argument("template", help="The prompt template", nargs="*")
        self.parser.add_argument(
            "-c",
            "--config",
            help="The prompt data in the format 'key=value'",
            nargs="*",
        )
        self.parser.add_argument("-d", "--data", help="The prompt data")
        self.parser.add_argument("-o", "--output", help="The txt file to generate")

    def execute(self, args):
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

        if not sys.stdin.isatty():
            args.template = sys.stdin.read().strip().splitlines() + args.template
        template = ", ".join(args.template)

        _logger.info(
            'Running template with input from "{0}" and data {1}'.format(template, data)
        )
        from ..services.template import TemplateService

        result = TemplateService().render(template, data)

        if args.output != None:
            os.makedirs(os.path.dirname(args.output), exist_ok=True)
            f = open(args.output, "w")
            f.write(result)
            f.close()
        else:
            print(result)
