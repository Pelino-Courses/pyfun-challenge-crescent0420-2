
from student import Student
from instructor import Instructor

class TeachingAssistant(Student, Instructor):
    def __init__(self, name: str, person_id: int, major: str, department: str):
        Student.__init__(self, name, person_id, major)
        Instructor.__init__(self, name, person_id, department)

    def get_role(self):
        return "Teaching Assistant"

