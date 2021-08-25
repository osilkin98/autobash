import sys
import os
import openai
from dotenv import load_dotenv
import json
import argparse

from src.utils import get_choices

load_dotenv()
openai.api_key = os.environ.get("OPENAI_KEY")


def get_arg_parser() -> argparse.ArgumentParser:
    """Creates an argument parser for the project"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'description',
        metavar='description',
        help='A Description of the command to be returned',
        type=str,
    )
    parser.add_argument(
        '--response_length',
        metavar='max_length',
        help='The maximum length of the response',
        type=int,
        default=140,
    )
    parser.add_argument(
        '--oneline',
        metavar='oneline',
        help='Whether the response should be on one line or not',
        type=bool,
        default=False
    )
    parser.add_argument(
        '--language',
        metavar='language',
        help='What language the response should be in',
        type=str,
        choices=['bash', 'ps', 'powershell'],
        default='bash',
        
    )
    return parser


def main(argv=None) -> str:
    """
    Takes the user's input and uses it to create a bash command
    """
    parser = get_arg_parser()
    args = parser.parse_args(argv)

    choices = get_choices(args.description, args.response_length)

    return json.dumps(choices, indent=2)


if __name__ == '__main__':
    sys.exit(main())
