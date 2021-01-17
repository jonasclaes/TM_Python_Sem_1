#  Jonas Claes <r0841639@student.thomasmore.be>
with open("../files/local_booking.txt") as file:
    classrooms = set()

    for line in file:
        record = line.rstrip().split(";")
        classrooms.add(record[3])

    print("Classrooms:")
    for classroom in classrooms:
        print(classroom)
