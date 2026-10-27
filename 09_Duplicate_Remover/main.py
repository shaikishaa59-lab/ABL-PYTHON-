# Duplicate Element Remover
# A set stores each distinct value once. The display order is sorted.

numbers_text = input("Enter integers separated by spaces: ")
parts = numbers_text.split()

if len(parts) == 0:
    print("Please enter at least one integer.")
else:
    numbers = []
    for part in parts:
        numbers.append(int(part))

    unique_numbers = set(numbers)
    print("Original list:", numbers)
    print("Unique elements:", sorted(unique_numbers))
