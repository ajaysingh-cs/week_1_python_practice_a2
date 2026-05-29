students = []

def add_student():
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student Added Successfully!")

def view_students():
    if not students:
        print("No Students Found!")
        return

    print("\nStudent Records:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")

def search_student():
    name = input("Enter Student Name to Search: ")

    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print(student)
            found = True

    if not found:
        print("Student Not Found!")

def delete_student():
    name = input("Enter Student Name to Delete: ")

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Program Closed")
        break
    else:
        print("Invalid Choice!")