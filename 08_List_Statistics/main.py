# List Statistics Calculator

numbers_text = input("Enter numbers separated by spaces: ")
parts = numbers_text.split()

if len(parts) == 0:
    print("Please enter at least one number.")
else:
    numbers = []
    for part in parts:
        numbers.append(float(part))

    total = 0
    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:
        total += number
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    average = total / len(numbers)

    print("Numbers:", numbers)
    print("Sum:", total)
    print("Average:", format(average, ".2f"))
    print("Largest:", largest)
    print("Smallest:", smallest)
