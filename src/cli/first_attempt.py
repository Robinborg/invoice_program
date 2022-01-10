import sys
sys.path.append("/Users/coalchewer/code/python/invoice_program/src")
from handlers import product_handler

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("square",
                    help = "enter a number to square",
                    type = int)
args = parser.parse_args()
print(args.square**2)

if len(sys.argv) <= 1:
    sys.argv.append("--help")

