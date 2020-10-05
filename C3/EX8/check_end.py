final_digit = int(input("What final digit do you want to check the numbers on: "))
counter = 0

for i in range(10):
    number = int(input("Enter a number: "))
    last_number = 0
    for j in str(number):
        last_number = int(j)
    if last_number == 7:
        counter += 1

print(counter, "out of 10 numbers end on 7")
