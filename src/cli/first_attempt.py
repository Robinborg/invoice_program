import argparse


parser = argparse.ArgumentParser()
parser.add_argument("square",
                    help = "enter a number to square",
                    type = int)
args = parser.parse_args()
print(args.square**2)

