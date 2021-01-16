#  Jonas Claes <r0841639@student.thomasmore.be>
with open("../files/contacts.csv") as file:
    # Read in all the contacts
    contacts = file.readlines()
    men = []
    women = []
    for contact in contacts:
        if contact != "\n":
            columns = contact.rstrip().split(";")
            # Check if man or woman
            if columns[3] == "M":
                men.append(columns)
            else:
                women.append(columns)

    # Sort and print all the women
    print(f"{len(women)} girls:")
    women = sorted(women, key=lambda x: x[1])
    for woman in women:
        print(f"\t{woman[1]} {woman[0]}")

    # Sort and print all the men
    print(f"{len(men)} boys:")
    men = sorted(men, key=lambda x: x[1])
    for man in men:
        print(f"\t{man[1]} {man[0]}")
