# Simple Calculator
# Topics used: input/output, type conversion, operators, if/elif.

first = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
second = float(input("Enter the second number: "))

if operator == "+":
    print("Result:", first + second)
elif operator == "-":
    print("Result:", first - second)
elif operator == "*":
    print("Result:", first * second)
elif operator == "/":
    if second == 0:
        print("Error: division by zero is not allowed.")
    else:
        print("Result:", first / second)
else:
    print("Invalid operator.")
