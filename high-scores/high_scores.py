"""
   This module offers a solution to
    the "High Scores" exercise on Exercism.io.
"""

import sys
from typing import List


def latest(scores: List[int]) -> int:
    return scores[-1]


def personal_best(scores: List[int]) -> int:
    return max(scores)


def personal_top_three(scores: List[int]) -> List[int]:
    return sorted(scores, reverse=True)[:3]


def main():

    def is_intstring(s:str) -> bool:
        try:
            int(s)
            return True
        except ValueError:
            return False

    argn_cmd = len(sys.argv)-1
    argv_cmd = sys.argv[1:]
    if argn_cmd >= 1 and all(is_intstring(s) for s in argv_cmd):
        lst:List[int] = [int(s) for s in argv_cmd]
        print(f"scores: {lst}")
        print(f"latest: {latest(lst)}")
        print(f"personal best: {personal_best(lst)}")
        print(f"personal top-three: {personal_top_three(lst)}")
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} int...")

if __name__ == '__main__':
    main()
