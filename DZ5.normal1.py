# import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int, action="store",
                    help="how many times must repeat the text")
parser.add_argument("s", action="store",
                    help="text to print")

args = parser.parse_args()

for _ in range(args.n):
    print(args.s)
