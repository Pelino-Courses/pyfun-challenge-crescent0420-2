
from student import Student
from instructor import Instructor
from course import Course
from enrollment import Enrollment
from teaching_assistant import TeachingAssistant

s1 = Student("Alice", 101, "CS")
s2 = Student("Bob", 102, "Math")
i1 = Instructor("Dr. Smith", 201, "CS")

ta1 = TeachingAssistant("Charlie", 103, "CS", "CS")

c1 = Course("CS101", "Intro to CS", 4)
c2 = Course("MATH201", "Calculus", 3)

c1.add_instructor(i1)
c1.add_student(s1)
c2.add_student(s2)
c1.add_student(ta1)
c1.add_instructor(ta1)

print(s1)
print(i1)
print(ta1)
print(c1)

for student in c1:
    print("Enrolled student:", student.name)

print("\nCourses Charlie is enrolled in:")
for course in ta1:
    print(course.title)
