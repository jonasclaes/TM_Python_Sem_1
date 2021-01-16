#  Jonas Claes <r0841639@student.thomasmore.be>
names_count = 0
starting_with_letter_count = 0
with open("../files/first_names.txt") as file:
    line = file.readline().rstrip()
    while line:
        if line != "\n":
            if line.rstrip().lower().find("z") != -1:
                print(line, end="")
                starting_with_letter_count += 1

            names_count += 1
        line = file.readline()

print(f"There are {names_count} first names in the file.")
print(f"{starting_with_letter_count} of which contain a letter z.")
