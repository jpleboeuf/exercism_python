"""
   This module offers a solution to
    the "Clock" exercise on Exercism.io.
"""

from __future__ import annotations
import sys


class Clock:
    """
        This class encapsulates a solution to the exercise:
         the initialization of the class,
         and the methods providing the solution.
    """

    def __init__(self, hour:int, minute:int):
        hour_carry, self.minute = divmod(minute, 60)
        day_carry, self.hour = divmod(hour + hour_carry, 24)

    def __repr__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other:Clock):
        return (self.hour == other.hour) and (self.minute == other.minute)

    def __add__(self, minutes:int):
        hour_carry, minute = divmod(self.minute + minutes, 60)
        day_carry, hour = divmod(self.hour + hour_carry, 24)
        return Clock(hour, minute)

    def __sub__(self, minutes:int):
        hour_uncarry, minute = divmod(self.minute - minutes, -60)
        day_uncarry, hour = divmod(self.hour - hour_uncarry, -24)
        return Clock(hour, minute)


def main():
    argn_cmd = len(sys.argv)-1
    argv_cmd = sys.argv[1:]

    try:
        if argn_cmd >= 1:
            clock = Clock(*(int(i) for i in argv_cmd[0].split(",")))
            if argn_cmd == 1:
                print(clock)
            elif argn_cmd == 2:
                if argv_cmd[1][0] in ("+", "-"):
                    print(clock + int(argv_cmd[1]))
                else:
                    raise SystemExit(f"Usage: {sys.argv[0]} H,M [+|-m]")
        else:
            raise SystemExit(f"Usage: {sys.argv[0]} H,M [+|-m]")
    except ValueError as ve:
        print("Problem encountered with some values:\n", ve)

if __name__ == '__main__':
    main()
