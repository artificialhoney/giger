import logging

_logger = logging.getLogger(__name__)


class RoopCommand:
    def __init__(self, parser):
        self.parser = parser.add_parser("roop", help="Swap faces")
        self.parser.add_argument(
            "-s", "--source", help="The source face image", required=True
        )
        self.parser.add_argument("-i", "--input", help="The input image", required=True)
        self.parser.add_argument(
            "-o", "--output", help="The output file", required=True
        )
        self.parser.add_argument("-m", "--model", help="The path to the model")

    def run(self, args):
        _logger.info(
            'Running Roop for "{0}" with "{1}"'.format(args.input, args.source)
        )
        from ..services.roop import RoopService

        RoopService().swap(args.source, args.input, args.output, args.model)
