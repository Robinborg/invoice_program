import sys
sys.path.append("/Users/coalchewer/code/python/invoice_program/src")
from handlers import product_handler

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-invoice',
                    action = "store_true")
args = parser.parse_args()

if len(sys.argv) <= 1:
    sys.argv.append("--help")

if args.a:
    product_handler.add_product()
else:
    print("jumped the function")

