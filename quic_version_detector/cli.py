import argparse


def parse_args(args):
    """Parses CLI arguments.

    Args:
        args (list): usually this will be sys.argv.
        description (string): Text to display before the argument help.

    Returns:
        Namespace: with host and port fields.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        metavar='HOSTNAME',
        dest='host',
        nargs='?',
        default='127.0.0.1',
        type=str,
        help='Server hostname or address.',
    )
    parser.add_argument(
        metavar='PORT',
        dest='port',
        nargs='?',
        default=443,
        type=int,
        help='QUIC server port.',
    )

    return parser.parse_args(args=args)
