year_of_birth = int(input("Enter your year of birth: "))

age = 2020 - year_of_birth

print("Your are " + str(age) + " years old.")

if age > 18:
    print("You're an adult.")
else:
    print("You're not an adult yet.")