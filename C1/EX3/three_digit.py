# Get number
three_digit_number = int(input("Enter a three-digit number: "))

print("Half = " + str(three_digit_number / 2))
print("Double = " + str(three_digit_number * 2))
print("Third power = " + str(three_digit_number ** 3))
print("Tenfold = " + str(three_digit_number * 10))

# Split number
print(three_digit_number // 100)
print(three_digit_number % 100 // 10)
print(three_digit_number % 10)
