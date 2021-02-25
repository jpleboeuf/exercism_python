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
        # Read the diagram of plants, split in 2 rows:
        diagram_rows = diagram.split("\n")
        #  and group the plants in tuples,
        #  each tuple containing the plants taken care of by a student:
        plant_groups = zip(*  #  (the tuple unpacking applies to the sum)
                # 2 plants from the first row:
                  [iter(diagram_rows[0])] * 2
                # and 2 plants from the second row:
                + [iter(diagram_rows[1])] * 2
            )
        student_i = iter(self.students)
        for plant_group in plant_groups:
            self.garden[next(student_i)] = list(map(Garden.plant.get, plant_group))

    def plants(self, child:str) -> List[str]:
        return self.garden[child]


def main():
    argn_cmd = len(sys.argv)-1
    argv_cmd = sys.argv[1:]

    def print_garden_foreach_student(garden:Garden):
        for student in garden.students:
            print(f"{student}: {garden.plants(student)}")

    def print_garden_for_student(garden:Garden, student:str):
        print(f"{garden.plants(student)}")

    def read_student_list(student_list:str) -> List[str]:
        return [s for s in student_list.split(",") if s != ""]

    if argn_cmd >= 1:
        argv_cmd_0_unesc = argv_cmd[0].replace("\\n", "\n")
        if argn_cmd == 1:
            garden = Garden(argv_cmd_0_unesc)
            print_garden_foreach_student(garden)
        elif argn_cmd == 2:
            if "," in argv_cmd[1]:
                garden = Garden(argv_cmd_0_unesc,
                    students=read_student_list(argv_cmd[1]))
                print_garden_foreach_student(garden)
            else:
                garden = Garden(argv_cmd_0_unesc)
                print_garden_for_student(garden, argv_cmd[1])
        elif argn_cmd == 3:
            garden = Garden(argv_cmd_0_unesc,
                students=read_student_list(argv_cmd[1]))
            print_garden_for_student(garden, argv_cmd[2])
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} diagram [students,] [student]")

if __name__ == '__main__':
    main()
