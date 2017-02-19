#!/usr/bin/env python

'''Convert Project Euler solution to base64 encoding for adding to tests.

Usage:
    convert <answer>
    convert (-h | --help)

Options:
    -h --help  Show this screen.

'''

from docopt import docopt
import base64


def convert(answer: str) -> bytes:
    return base64.b64encode(answer.encode())


if __name__ == '__main__':
    arguments = docopt(__doc__)

    print(convert(arguments["<answer>"]))
