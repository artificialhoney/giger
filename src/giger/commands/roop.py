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
        self.parser.add_argument(
            "-e", "--enhance", help="Enhance face", action="store_true"
        )
        self.parser.add_argument("-g", "--gfpgan_path", help="GFPGAN model path")
        self.parser.add_argument("-dw", "--determined_width", default=640, type=int)
        self.parser.add_argument("-dh", "--determined_height", default=640, type=int)
        self.parser.add_argument("-t", "--input_target", default=0, type=int)

    def execute(self, args):
        _logger.info('Running Roop for "{0}" with "{1}"'.format(args.input, args.face))

        from ..services.roop import RoopService

        RoopService().swap(
            args.face,
            args.input,
            args.output,
            model=args.model,
            enhance=args.enhance,
            gfpgan_path=args.gfpgan_path,
            det_size=(args.determined_width, args.determined_height),
            input_target=args.input_target,
        )
