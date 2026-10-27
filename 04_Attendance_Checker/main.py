# Student Attendance Eligibility Checker
# Example eligibility threshold: 75 percent.

total_classes = int(input("Enter total classes held: "))
attended_classes = int(input("Enter classes attended: "))

if total_classes <= 0:
    print("Total classes must be greater than zero.")
elif attended_classes < 0 or attended_classes > total_classes:
    print("Invalid number of attended classes.")
else:
    percentage = attended_classes / total_classes * 100
    print("Attendance percentage:", format(percentage, ".2f") + "%")

    if percentage >= 75:
        print("Eligibility: Eligible")
    else:
        print("Eligibility: Not eligible")
