"""
   This module offers a solution to
    the "Isogram" exercise on Exercism.io.
"""

import sys
from typing import List


def is_isogram(string:str) -> bool:

    def alpha_pos(c:str) -> int:
        return ord(c) - ord("A") + 1

    alphagram: List[int] = [None] + [0] * 26
    for c in string:
        if c.isalpha():
            c_l_ap = alpha_pos(c.upper())
            alphagram[c_l_ap] += 1
            if alphagram[c_l_ap] > 1:
                return False
    return True


def main():
    argn_cmd = len(sys.argv)-1
    argv_cmd = sys.argv[1:]
    def is_or_isnt_an_isogram(word:str) -> str:
        return "is" \
            + ("" if is_isogram(word) else " not") \
            + " an isogram"
    if argn_cmd == 1:
        print(f"{argv_cmd[0]} {is_or_isnt_an_isogram(argv_cmd[0])}")
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} word")

if __name__ == '__main__':
    main()
