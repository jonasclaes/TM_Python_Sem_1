#  Jonas Claes <r0841639@student.thomasmore.be>
with open("../files/first_names.txt") as file:
    first_names = file.readlines()
    for i in range(0, len(first_names), 10):
        for first_name in first_names[i:i+10]:
            first_name = first_name.rstrip().ljust(13)
            print(first_name, end="")
        print()
