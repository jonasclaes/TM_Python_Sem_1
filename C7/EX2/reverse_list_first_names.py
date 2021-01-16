#  Jonas Claes <r0841639@student.thomasmore.be>
with open("../files/first_names.txt") as file:
    first_names = file.readlines()
    first_names.reverse()
    for first_name in first_names:
        if first_name != "\n":
            print(first_name, end="")
