"""
   This module offers a solution to
    the "Luhn" exercise on Exercism.io.
"""

import sys


class Luhn:

    def __init__(self, num:str):
        self.num = num

    def valid(self) -> bool:

        # Except space, all other non-digit characters are disallowed:
        for c in self.num:
            if not (c.isdigit() or c == ' '):
                return False
        # Strip spaces:
        num_clean: str = ''.join(c for c in self.num if c.isdigit())
        # Strings of length 1 or less are not valid:
        if len(num_clean) <= 1:
            return False

        num_tmp: str = ""
        # Step 1:
        for i, c in enumerate(reversed(num_clean), 1):
            d: int = 0
            if i % 2 == 0:
                d2: int = int(c) * 2
                d = d2 if d2 <= 9 else d2 - 9
            else:
                d = int(c)
            num_tmp = str(d) + num_tmp
        # Step 2:
        num_sum:int = sum(int(c) for c in num_tmp)
        # Test:
        return num_sum % 10 == 0


def main():
    argn_cmd = len(sys.argv)-1
    argv_cmd = sys.argv[1:]
    if argn_cmd == 1:
        l = Luhn(argv_cmd[0])
        print(f"Luhn algorithm validation result → {'not ' if not l.valid() else ''}valid.")
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} number")

if __name__ == '__main__':
    main()
