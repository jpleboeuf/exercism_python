"""
   This module offers a solution to
    the "Luhn" exercise on Exercism.io.
"""

import sys
from enum import Enum
from typing import List


class Luhn:

    class NumStatus(Enum):
        DIRTY_CHR = 1
        DIRTY_LEN = 2
        NOT_DIRTY = 3
        NOT_VALID = 4
        VALID = 5

    def __init__(self, num_in:str):
        self.num_in:str = num_in
        self.num_in_status:Luhn.NumStatus = None
        try:
            self.clean_num_in()
            self.num_in_status = Luhn.NumStatus.NOT_DIRTY
        except ValueError as val_err:
            print(val_err)

    def clean_num_in(self):
        # Except space, all other non-digit characters are disallowed:
        for c in self.num_in:
            if not (c.isdigit() or c == ' '):
                self.num_in_status = Luhn.NumStatus.DIRTY_CHR
                raise ValueError(f"{self.num_in}: non-digit characters are disallowed!")
        # Strip spaces:
        self.num: str = ''.join(c for c in self.num_in if c.isdigit())
        # Strings of length 1 or less are not valid:
        if len(self.num) <= 1:
            self.num_in_status = Luhn.NumStatus.DIRTY_LEN
            raise ValueError(f"{self.num}: a string of length 1 or less is not valid!")

    def valid(self) -> bool:

        if self.num_in_status != Luhn.NumStatus.NOT_DIRTY:
            return False

        num_digits: List[int] = [int(c) for c in self.num]
        # Step 1:
        num_2_digits: List[int] = []
        for i, d in enumerate(reversed(num_digits), 1):
            d_2: int = d
            if i % 2 == 0:
                d_2_dbl: int = d_2 * 2
                d_2 = d_2_dbl if d_2_dbl <= 9 else d_2_dbl - 9
            num_2_digits.insert(0, d_2)
        # Step 2:
        num_2_digits_sum: int = sum(d_2 for d_2 in num_2_digits)
        # Step 3:
        return num_2_digits_sum % 10 == 0


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
