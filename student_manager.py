from student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, age):
        student = Student(name, age)
        self.students.append(student)

    def get_students(self):
        return self.students
