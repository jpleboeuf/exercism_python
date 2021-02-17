"""
   This module offers a solution to
    the "Kindergarten Garden" exercise on Exercism.io.
"""

import sys
from typing import List, Dict, Final


class Garden:
    """
        This class encapsulates a solution to the exercise:
         some definitions, the initialization of the class,
         the method providing the solution.
    """

    # typing.Final not supported by pylint at this time
    #  https://github.com/PyCQA/pylint/issues/3197

    children:Final[List[str]] = [  # pylint: disable=unsubscriptable-object
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eve",
            "Fred",
            "Ginny",
            "Harriet",
            "Ileana",
            "Joseph",
            "Kincaid",
            "Larry",
        ]

    plant:Final[Dict[str, str]] = {  # pylint: disable=unsubscriptable-object
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets",
        }

    def __init__(self, diagram:str, students=None):
        self.students: List[str] =\
            sorted(students) if students is not None else Garden.children
        self.garden: Dict[str, List[str]] =\
            { student: [] for student in self.students }
        diagram_rows = diagram.split("\n")
        for dr_idx in range(0, len(diagram_rows[0]), 2):
            self.garden[self.students[dr_idx // 2]] = [
                    Garden.plant[diagram_rows[dr][dri]]
                        for dr in (0, 1) for dri in (dr_idx, dr_idx+1)
                ]

    def plants(self, child:str) -> List[str]:
        return self.garden[child]


def main():
    argn_cmd = len(sys.argv)-1
    argv_cmd = sys.argv[1:]
    if argn_cmd >= 1:
        if argn_cmd == 1:
            garden = Garden(argv_cmd[0].replace("\\n", "\n"))
            for student in garden.students:
                print(f"{student}: {garden.plants(student)}")
        elif argn_cmd == 2:
            if "," in argv_cmd[1]:
                garden = Garden(argv_cmd[0].replace("\\n", "\n"),
                    students=[s for s in argv_cmd[1].split(",") if s != ""])
                for student in garden.students:
                    print(f"{student}: {garden.plants(student)}")
            else:
                garden = Garden(argv_cmd[0].replace("\\n", "\n"))
                print(f"{garden.plants(argv_cmd[1])}")
        elif argn_cmd == 3:
            garden = Garden(argv_cmd[0].replace("\\n", "\n"),
                students=[s for s in argv_cmd[1].split(",") if s != ""])
            print(f"{garden.plants(argv_cmd[2])}")
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} diagram [students,] [student]")

if __name__ == '__main__':
    main()
