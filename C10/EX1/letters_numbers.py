#  Jonas Claes <r0841639@student.thomasmore.be>
text = input("Enter a text consisting only of letters and numbers: ")

numbers = set()
letters = set()
for char in text:
    if char.isnumeric():
        numbers.add(char)
    else:
        letters.add(char)

print("The numbers:")
for number in numbers:
    print(number)
print("The letters:")
for letter in letters:
    print(letter)
