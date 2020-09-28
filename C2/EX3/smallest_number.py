first_number = int(input("First number: "))
second_number = int(input("Second number: "))
third_number = int(input("Third number: "))

smallest_number = 0

if first_number < second_number:
    if first_number < third_number:
        smallest_number = first_number
    else:
        smallest_number = third_number
else:
    if second_number < third_number:
        smallest_number = second_number
    else:
        smallest_number = third_number

print("The smallest number is " + str(smallest_number))