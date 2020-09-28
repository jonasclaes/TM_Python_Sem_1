first_number = int(input("First number: "))
second_number = int(input("Second number: "))
third_number = int(input("Third number: "))

if first_number + second_number == third_number:
    print("This works")
elif second_number + third_number == first_number:
    print("This works")
elif first_number + third_number == second_number:
    print("This works")
else:
    print("This won't work")