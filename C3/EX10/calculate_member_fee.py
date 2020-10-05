for i in range(1, 5):
    print("Information for member", i)
    name = input("Name: ")
    age = int(input("Age: "))
    membership_time = int(input("Member for how many years: "))

    price_in_euros = 0

    if age < 12:
        price_in_euros = 20
    elif 12 <= age <= 18:
        price_in_euros = 50
    else:
        price_in_euros = 95

    if membership_time > 5:
        price_in_euros *= 0.9

    print("Member fee for", name, "=", price_in_euros)
    print()
