# Simple Calculator

first = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
second = float(input("Enter the second number: "))

if operator == "+":
    answer = first + second
    print("Result:", answer)
elif operator == "-":
    answer = first - second
    print("Result:", answer)
elif operator == "*":
    answer = first * second
    print("Result:", answer)
elif operator == "/":
    if second == 0:
        print("Error: division by zero is not allowed.")
    else:
        answer = first / second
        print("Result:", answer)
else:
    print("Invalid operator.")
