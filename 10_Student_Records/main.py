# Student Records Using Lists and Tuples
# Each student record is stored as a tuple: (name, marks).

students = []
count = int(input("How many students? "))

if count <= 0:
    print("Enter a number of students greater than zero.")
else:
    for index in range(count):
        name = input("Enter student name: ")
        marks = float(input("Enter marks for " + name + ": "))
        students.append((name, marks))

    print("\nStudent Records")
    for student in students:
        name, marks = student
        print("Name:", name, "| Marks:", marks)

    highest_student = students[0]
    for student in students:
        if student[1] > highest_student[1]:
            highest_student = student

    print("\nHighest scorer:", highest_student[0])
    print("Highest marks:", highest_student[1])
