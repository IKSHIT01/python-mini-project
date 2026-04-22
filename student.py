students = {}

def add_student():
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
    print("Student added successfully!")

def view_students():
    if not students:
        print("No records found")
    else:
        for name, marks in students.items():
            print(f"{name} : {marks}")

def search_student():
    name = input("Enter name to search: ")
    if name in students:
        print(f"{name} found with marks {students[name]}")
    else:
        print("Student not found")

def delete_student():
    name = input("Enter name to delete: ")
    if name in students:
        del students[name]
        print("Deleted successfully")
    else:
        print("Student not found")

while True:
    print("\n1. Add\n2. View\n3. Search\n4. Delete\n5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice")
