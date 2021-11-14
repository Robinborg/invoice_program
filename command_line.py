import sys


def ask_user():
    """Take users input from the command-line"""
    try:
        cl_input = sys.argv[1]
    except IndexError:
        raise SystemExit(f"You didn't enter command for {sys.argv[0]}")
    return cl_input



