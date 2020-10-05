smallest_number = 0
biggest_number = 0

number = int(input("Enter a number: "))

while number != 0:
    if number < smallest_number:
        smallest_number = number
    elif number > biggest_number:
        biggest_number = number
    number = int(input("Enter a number: "))
print("The difference between the largest number", biggest_number, "and the smallest", smallest_number, "=", biggest_number-smallest_number)