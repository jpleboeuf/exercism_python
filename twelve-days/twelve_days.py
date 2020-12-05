"""
   This module offers a solution to
    the "Twelve Days" exercise on Exercism.io.
"""

import sys
from typing import List


def recite(start_verse: int, end_verse:int) -> List[str]:
    verse: List[str] = []
    # Ordinal numerals:
    on: List[str] = [ "zerost", "first", "second", "third",\
                      "fourth", "fifth", "sixth" , "seventh",\
                      "eighth", "ninth", "tenth", "eleventh",\
                      "twelfth" ]
    present: List[str] = [ None,
                            "a Partridge in a Pear Tree",
                            "two Turtle Doves",
                            "three French Hens",
                            "four Calling Birds",
                            "five Gold Rings",
                            "six Geese-a-Laying",
                            "seven Swans-a-Swimming",
                            "eight Maids-a-Milking",
                            "nine Ladies Dancing",
                            "ten Lords-a-Leaping",
                            "eleven Pipers Piping",
                            "twelve Drummers Drumming"
                           ]
    for vn in range(start_verse, end_verse+1):
        v = f"On the {on[vn]} day of Christmas my true love gave to me: "
        for p in range(vn, 0, -1):
            v += ("and " if (p == 1 and vn != 1) else "")\
                + present[p]\
                + (", " if p != 1 else ".")
        verse.append(v)
    return verse


def main():

    def is_intstring(s:str) -> bool:
        try:
            int(s)
            return True
        except ValueError:
            return False

    class ArgumentError(Exception):
        pass

    argn_cmd = len(sys.argv)-1
    argv_cmd = sys.argv[1:]
    start_verse = 0
    end_verse = 0
    try:
        if argn_cmd == 0:
            start_verse = 1
            end_verse = 12
        elif argn_cmd == 2:
            if is_intstring(argv_cmd[0]) and is_intstring(argv_cmd[1]):
                start_verse = int(argv_cmd[0])
                end_verse = int(argv_cmd[1])
                if start_verse not in range(1, 13)\
                   or end_verse not in range(1, 13):
                    raise ValueError(\
                        "start_verse and end_verse must be between 1 and 12")
                elif end_verse < start_verse:
                    raise ValueError(\
                        "start_verse must be before end_verse")
            else:
                raise ArgumentError()
        else:
            raise ArgumentError()
    except ArgumentError as ae:
        raise SystemExit(\
            f"Usage: {sys.argv[0]} [start_verse:int end_verse:int]")\
            from ae
    for verse in recite(start_verse, end_verse):
        print(verse)

if __name__ == '__main__':
    main()
