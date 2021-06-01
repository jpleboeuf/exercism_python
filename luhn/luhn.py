"""
   This module offers a solution to
    the "Luhn" exercise on Exercism.io.
"""

import sys


class Luhn:

    def __init__(self, num_in:str):
        self.num_in = num_in
        self.num_in_not_clean = True
        try:
            self.clean_num_in()
            self.num_in_not_clean = False
        except ValueError as ve:
            print(ve)

    def clean_num_in(self):
        # Except space, all other non-digit characters are disallowed:
        for c in self.num_in:
            if not (c.isdigit() or c == ' '):
                raise ValueError(f"{self.num_in}: non-digit characters are disallowed!")
        # Strip spaces:
        self.num: str = ''.join(c for c in self.num_in if c.isdigit())
        # Strings of length 1 or less are not valid:
        if len(self.num) <= 1:
            raise ValueError(f"{self.num}: a string of length 1 or less is not valid!")

    def valid(self) -> bool:

        if self.num_in_not_clean:
            return False

        num_tmp: str = ""
        # Step 1:
        for i, c in enumerate(reversed(self.num), 1):
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
