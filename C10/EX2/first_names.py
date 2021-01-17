#  Jonas Claes <r0841639@student.thomasmore.be>
def get_first_names(filepath: str):
    file = open(filepath)
    names = set()
    count = 0
    for line in file:
        if line != "\n":
            count += 1
            names.add(line.rstrip())
    file.close()
    return count, names


amount_of_names_1itf, unique_names_1itf = get_first_names("../files/first_names1ITF.txt")
print(f"In 1ITF there are {len(unique_names_1itf)} different first names")
amount_of_names_2itf, unique_names_2itf = get_first_names("../files/first_names2ITF.txt")
print(f"In 2ITF there are {len(unique_names_2itf)} different first names")

unique_names = sorted(list(unique_names_1itf | unique_names_2itf))

print("These are the first 51 names appearing in 1ITF and 2ITF")
for i in range(0, 51):
    print(unique_names[i])
