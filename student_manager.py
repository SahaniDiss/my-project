from student import Student

class StudentManager:
    def __init__(self):
        self.students_list = []

    def add_student(self, name, age):
        student = Student(name, age)
        self.students_list.append(student)

    def remove_student(self, name):
        self.students_list = [student for student in self.students_list if student.name != name]

    def get_students(self):
        return self.students_list
