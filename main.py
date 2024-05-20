from student_manager import StudentManager

if __name__ == "__main__":
    manager = StudentManager()

    # Adding students
    manager.add_student("Alice", 20)
    manager.add_student("Bob", 22)
    manager.add_student("Charlie", 25)

    # To Retrieve and print students
    students = manager.get_students()
    for student in students:
        print(student)
