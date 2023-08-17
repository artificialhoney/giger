import logging

_logger = logging.getLogger(__name__)


class RoopCommand:
    def __init__(self, parser):
        self.parser = parser.add_parser("roop", help="Swap faces")
        self.parser.add_argument(
            "-f", "--face", help="The source face image", required=True
        )
        self.parser.add_argument("-i", "--input", help="The input image", required=True)
        self.parser.add_argument(
            "-o", "--output", help="The output file", required=True
        )
        self.parser.add_argument("-m", "--model", help="The path to the model")

    def execute(self, args):
        _logger.info('Running Roop for "{0}" with "{1}"'.format(args.input, args.face))

        from ..services.roop import RoopService

        RoopService().swap(args.face, args.input, args.output, args.model)
