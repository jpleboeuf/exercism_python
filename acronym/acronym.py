"""
   This module offers a solution to
    the "Acronym" exercise on Exercism.io.
"""

import sys
from typing import List


def abbreviate(words:str) -> str:
    real_words: List[str] = "".join(
            [c if (c.isalpha() or c == "'") else " " for c in words]
        ).split()
    return "".join([w[0].upper() for w in real_words])


def main():
    argn_cmd = len(sys.argv)-1
    argv_cmd = sys.argv[1:]
    if argn_cmd == 1:
        print(f"{abbreviate(argv_cmd[0])}")
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} words")

if __name__ == '__main__':
    main()
