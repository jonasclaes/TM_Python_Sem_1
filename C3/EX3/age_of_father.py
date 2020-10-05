age = int(input("How old are you: "))
age_father = int(input("How old is your father: "))

counter = 0
solution_found = False

while not solution_found and counter < 100:
    if (age + counter) == (age_father + counter) / 2:
        solution_found = True
    else:
        counter += 1

if solution_found:
    print("Within " + str(counter) + " years your father will have twice your age")
else:
    print("The situation is no longer possible for your ages")
