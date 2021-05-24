"""
   This module offers a solution to
    the "Grade School" exercise on Exercism.io.
"""

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
