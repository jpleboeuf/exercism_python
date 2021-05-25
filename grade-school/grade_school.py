"""
   This module offers a solution to
    the "Grade School" exercise on Exercism.io.
"""

import sys
from typing import List
from operator import attrgetter

class School:
    """
        This class encapsulates a solution to the exercise:
         a sub-class definition, the initialization of the class,
         the methods providing the solution.
    """

    class Student:
        """
            This class defines the properties attached to a student.
        """

        def __init__(self, name:str, grade:int):
            self.name: str = name
            self.grade: int = grade

    def __init__(self):
        self.students:List[School.Student] = []

    def add_student(self, name:str, grade:int):
        self.students.append(School.Student(name, grade))
        self.students.sort(key=attrgetter('grade', 'name'))

    def roster(self) -> List[str]:
        return [s.name for s in self.students]

    def grade(self, grade_number) -> List[str]:
        return [s.name for s in self.students if s.grade==grade_number]

def main():
    argn_cmd = len(sys.argv)-1
    argv_cmd = sys.argv[1:]

    def print_student_names(student_names:List[str]):
        print(", ".join(student_names))

    def read_student_list(student_list:str) -> List[str]:
        return [School.Student(*s.split(":"))
            for s in student_list.split(",") if s != ""]

    if argn_cmd >= 1:
        students = read_student_list(argv_cmd[0])
        school = School()
        for student in students:
            school.add_student(student.name, student.grade)
        if argn_cmd == 1:
            print_student_names(school.roster())
        elif argn_cmd == 2:
            print_student_names(school.grade(argv_cmd[1]))
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} student_name:student_grade, [grade_number]")

if __name__ == '__main__':
    main()
