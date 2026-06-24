students = {}

def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    marks = int(input("Enter Marks: "))

    students[roll] = {
        "Name": name,
        "Marks": marks
    }

def display_students():
    for roll, data in students.items():
        print("Roll No:", roll)
        print("Name:", data["Name"])
        print("Marks:", data["Marks"])
        print()

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        break
    else:
        print("Invalid Choice")