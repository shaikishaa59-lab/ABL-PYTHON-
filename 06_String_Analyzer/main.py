# String Analyzer

text = input("Enter a sentence: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0

for character in text:
    if character.lower() in "aeiou":
        vowels += 1
    elif character.isalpha():
        consonants += 1
    elif character.isdigit():
        digits += 1
    elif character == " ":
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
