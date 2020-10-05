number = int(input("Enter a number, stop by entering a zero: "))
total = 1
numbers_entered = 0

while number != 0:
    numbers_entered += 1
    total *= number
    number = int(input("Enter a number, stop by entering a zero: "))
print("The product of the " + str(numbers_entered) + " numbers is " + str(total))
