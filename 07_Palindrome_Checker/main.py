# Palindrome Checker
# Spaces and letter case are ignored.

word = input("Enter a word or sentence: ")
cleaned = word.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
