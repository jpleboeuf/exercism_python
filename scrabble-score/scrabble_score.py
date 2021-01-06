"""
   This module offers a solution to
       the "Scrabble Score" exercise on Exercism.io.
"""

import sys
from typing import Dict


def init_letter_values() -> Dict[str, int]:
    letter_values = [
            (["A", "E", "I", "O", "U",\
              "L", "N", "R", "S", "T"],  1),
            (["D", "G"],                 2),
            (["B", "C", "M", "P"],       3),
            (["F", "H", "V", "W", "Y"],  4),
            (["K"],                      5),
            (["J", "X"],                 8),
            (["Q", "Z"],                10),
        ]
    lv = {}
    for letters, value in letter_values:
        for letter in letters:
            lv[letter] = value
    return lv

lv = init_letter_values()

def score(word:str) -> int:
     return sum([lv[l] for l in word.upper()])


def main():
    argn_cmd = len(sys.argv)-1
    argv_cmd = sys.argv[1:]
    if argn_cmd == 1:
        print(f"{argv_cmd[0]} {score(argv_cmd[0])}")
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} word")

if __name__ == '__main__':
    main()
