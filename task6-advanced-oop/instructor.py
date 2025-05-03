# instructor.py
from person import Person

class Instructor(Person):
    def __init__(self, name: str, person_id: int, department: str):
        super().__init__(name, person_id)
        self.department = department
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

    def __iter__(self):
        return iter(self.courses)

    def get_role(self):
        return "Instructor"

