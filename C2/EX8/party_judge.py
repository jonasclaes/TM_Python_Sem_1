bottles_of_wine = int(input("How many bottles of wine are there: "))
amount_of_pizzas = int(input("How many pizzas are there: "))

if amount_of_pizzas >= 5 and bottles_of_wine >= 5:
    if amount_of_pizzas >= bottles_of_wine * 2 or bottles_of_wine >= amount_of_pizzas * 2:
        print("This is a fantastic party")
    else:
        print("This is a good party")
else:
    print("This is just a stupid party")
