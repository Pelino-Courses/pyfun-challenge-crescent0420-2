from person import Person

class Student(Person):
    def __init__(self, name: str, person_id: int, major: str):
        super().__init__(name, person_id)
        self.major = major
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def __iter__(self):
        return iter(self.courses)

    def get_role(self):
        return "Student"
