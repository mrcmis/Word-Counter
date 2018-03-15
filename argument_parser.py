import argparse
import config


def set_parser():
    """
    setting up parser
    """
    parser = argparse.ArgumentParser(description=config.program_terminal_desc)
    parser.add_argument('file', nargs='?', type=str, help='file to be opened', default=' ')
    parser.add_argument('-l', '--lines', help='counting lines', action='store_true')
    parser.add_argument('-w', '--words', help='counting words', action='store_true')
    parser.add_argument('-c', '--chars', help='counting chars', action='store_true')

    return parser
