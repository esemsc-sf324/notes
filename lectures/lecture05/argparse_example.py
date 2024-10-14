#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="A minimal argparse example.")
parser.add_argument('name', type=str, help='Your name')
parser.add_argument('-a', '--age', type=int, help='Your age', default=0)

args = parser.parse_args()

print(f"Hello, {args.name}!")
if args.age:
    print(f"You are {args.age} years old.")
