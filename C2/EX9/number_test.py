number_1 = int(input("number 1 (0, 1 or 2): "))
number_2 = int(input("number 2 (0, 1 or 2): "))
number_3 = int(input("number 3 (0, 1 or 2): "))

if (number_1 == number_2 == number_3):
    if (number_1 == 2):
        print(10)
    else:
        print(5)
elif number_2 == number_3 and number_1 != number_2:
    print(1)
else:
    print(0)