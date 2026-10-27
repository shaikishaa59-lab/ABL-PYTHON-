# Student Grade Calculator
# Assumption: five subjects, each marked out of 100; pass mark is 35 in each subject.

marks = []
for subject in range(1, 6):
    mark = int(input("Enter marks for subject " + str(subject) + " (0-100): "))
    while mark < 0 or mark > 100:
        print("Marks must be between 0 and 100.")
        mark = int(input("Re-enter marks for subject " + str(subject) + ": "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

print("\nTotal marks:", total, "out of 500")
print("Percentage:", format(percentage, ".2f") + "%")

if min(marks) < 35:
    print("Result: Fail")
    print("Grade: F")
elif percentage >= 90:
    print("Result: Pass")
    print("Grade: A")
elif percentage >= 75:
    print("Result: Pass")
    print("Grade: B")
elif percentage >= 60:
    print("Result: Pass")
    print("Grade: C")
elif percentage >= 35:
    print("Result: Pass")
    print("Grade: D")
else:
    print("Result: Fail")
    print("Grade: F")
