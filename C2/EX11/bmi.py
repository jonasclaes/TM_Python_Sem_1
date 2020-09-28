weight_in_kg = float(input("Weight in kilograms: "))
length_in_cm = float(input("Length in centimetres: "))

bmi = (weight_in_kg / length_in_cm ** 2) * 10000

print("A person of " + str(weight_in_kg) + " kg with a length of " + str(length_in_cm) + " cm has a BMI of " + str(bmi))

if bmi < 18:
    print("This is underweight.")
elif 18 <= bmi < 25:
    print("This is a normal weight.")
elif 25 <= bmi < 27:
    print("This is slightly overweight")
elif 27 <= bmi < 30:
    print("This is moderately overweight")
elif 30 <= bmi < 40:
    print("This is obese")
else:
    print("This is sickly obese")
