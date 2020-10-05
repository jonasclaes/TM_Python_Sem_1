number = int(input("Enter a number: "))
zeroes = 0
sixes = 0

for char in str(number):
    if int(char) == 0:
        zeroes += 1
    elif int(char) == 6:
        sixes += 1
print("The number consists of " + str(zeroes) + " zeros and " + str(sixes) + " sixes")
