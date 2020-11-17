"""
   This module offers a solution to
    the "Two Fer" exercise on Exercism.io.
"""

import sys


def two_fer(name:str = "you") -> str:
    return f"One for {name}, one for me."


def main():
    argn = len(sys.argv)
    if argn == 1:
        print(two_fer())
    elif argn == 2:
        print(two_fer(sys.argv[1]))
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} [name]")

if __name__ == '__main__':
    main()
