# Multiplication Table Generator

number = int(input("Enter a number: "))
limit = int(input("Enter the table limit: "))

if limit <= 0:
    print("The table limit must be greater than zero.")
else:
    for multiplier in range(1, limit + 1):
        print(number, "x", multiplier, "=", number * multiplier)
