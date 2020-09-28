number_1 = int(input("First number: "))
number_2 = int(input("Second number: "))

if 30 <= number_1 <= 40 and 30 <= number_2 <= 40:
    print("Both numbers are ok")
elif number_1 in [65, 72, 83, 90] and number_2 in [65, 72, 83, 90]:
    print("Both numbers are ok")
else:
    print("They are NOT ok")
