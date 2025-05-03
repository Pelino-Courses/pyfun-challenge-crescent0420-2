
class Enrollment:
    def __init__(self):
        self.records = {}

    def enroll(self, student, course):
        if student not in self.records:
            self.records[student] = []
        if course not in self.records[student]:
            self.records[student].append(course)
            course.add_student(student)

    def get_courses(self, student):
        return self.records.get(student, [])
