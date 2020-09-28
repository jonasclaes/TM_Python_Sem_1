first_number = int(input("First number: "))
second_number = int(input("Second number: "))

if first_number == second_number:
    print("The answer for the numbers " + str(first_number) + " and " + str(second_number) + " = 0")
elif first_number % 5 == 0 and second_number % 5 == 0:
    if first_number < second_number:
        print("The answer for the numbers " + str(first_number) + " and " + str(second_number) + " = " + str(first_number))
    else:
        print("The answer for the numbers " + str(first_number) + " and " + str(second_number) + " = " + str(second_number))
else:
    if first_number < 0:
        first_number = -first_number

    if second_number < 0:
        second_number = -second_number

    if first_number > second_number:
        print("The answer for the numbers " + str(first_number) + " and " + str(second_number) + " = " + str(first_number))
    else:
        print("The answer for the numbers " + str(first_number) + " and " + str(second_number) + " = " + str(second_number))


