#  Jonas Claes <r0841639@student.thomasmore.be>
with open("../files/hamlet.txt") as input_file:
    with open("hamlet2.txt", "w") as output_file:
        lines = input_file.readlines()
        for line in lines:
            previous_character = line[0]
            for i in range(0, len(line)):
                if previous_character in (",", ".", "...", "!") and line[i] == " " and line[i+1] == " ":
                    continue
                output_file.write(line[i])
                previous_character = line[i]
