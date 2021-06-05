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
            if not (c.isdigit() or c == " "):
                self.num_in_status = Luhn.NumStatus.DIRTY_CHR
                raise ValueError(f"{self.num_in}: non-digit characters are disallowed!")
        # Strip spaces:
        self.num: str = ''.join(c for c in self.num_in if c.isdigit())
        # Numeric strings of length 1 or less are not valid:
        if len(self.num) <= 1:
            self.num_in_status = Luhn.NumStatus.DIRTY_LEN
            raise ValueError(f"{self.num}: a numeric string of length 1 or less is not valid!")

    def valid(self) -> bool:

        if self.num_in_status.value < Luhn.NumStatus.NOT_DIRTY.value:
            return False

        addends: List[int] = [int(c) for c in self.num]
        # Step 1:
        for i in range(len(addends)-2, -1, -2):
            # Loop
            #  from the rightmost digit (excluding the check digit),
            #  to the leftmost digit,
            #  moving left and taking into account every second digit:
            addends[i] *= 2
            if addends[i] > 9:
                addends[i] -= 9
        # Step 2:
        addends_sum: int = sum(a for a in addends)
        # Step 3:
        check_sum: int = addends_sum % 10
        if check_sum == 0:
            self.num_in_status = Luhn.NumStatus.VALID
        else:
            self.num_in_status = Luhn.NumStatus.NOT_VALID
        return self.num_in_status == Luhn.NumStatus.VALID


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
