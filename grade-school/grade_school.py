from operator import attrgetter

class School:

    class Student:

        def __init__(self, name, grade):
            self.name = name
            self.grade = grade

    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        self.students.append(School.Student(name, grade))
        self.students.sort(key=attrgetter('grade', 'name'))

    def roster(self):
        return [s.name for s in self.students]

    def grade(self, grade_number):
        return [s.name for s in self.students if s.grade==grade_number]
