import sys
from typing import  List


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
    
    argn = len(sys.argv)-1
    argv = sys.argv[1:]
    if argn >= 1 and all(is_intstring(s) for s in argv):
        lst:List[int] = [int(s) for s in argv]
        print(lst)
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} int...")

if __name__ == '__main__':
    main()
