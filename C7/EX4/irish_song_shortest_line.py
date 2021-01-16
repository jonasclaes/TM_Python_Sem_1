#  Jonas Claes <r0841639@student.thomasmore.be>
with open("../files/irish_song.txt") as file:
    line = file.readline()
    shortest_line = line.rstrip()
    shortest_line_characters = len(line.rstrip())
    line = file.readline()
    while line:
        if len(line.rstrip()) < shortest_line_characters:
            shortest_line = line.rstrip()
            shortest_line_characters = len(line.rstrip())
        line = file.readline()

    print(f"The shortest line has {shortest_line_characters} characters")
    print(shortest_line)
