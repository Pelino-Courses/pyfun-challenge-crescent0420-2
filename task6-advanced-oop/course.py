
class Course:
    def __init__(self, code: str, title: str, credits: int):
        self.code = code
        self.title = title
        self.credits = credits
        self.students = []
        self.instructors = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.enroll(self)

    def add_instructor(self, instructor):
        if instructor not in self.instructors:
            self.instructors.append(instructor)
            instructor.assign_course(self)

    def __str__(self):
        return f"{self.code}: {self.title} ({self.credits} credits)"

    def __iter__(self):
        return iter(self.students)

    @classmethod
    def from_dict(cls, data):
        return cls(data['code'], data['title'], data['credits'])

