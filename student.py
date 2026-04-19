# Simple Student Management System

students = {}

def add_student():
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    students[name] = marks
    print("Student added!")

def view_students():
    for name, marks in students.items():
        print(name, ":", marks)

while True:
    print("\n1. Add Student\n2. View Students\n3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        break
    else:
        print("Invalid choice")
