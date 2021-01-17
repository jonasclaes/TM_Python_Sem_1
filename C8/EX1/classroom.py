#  Jonas Claes <r0841639@student.thomasmore.be>
with open("../files/classrooms.txt") as file:
    line = file.readline().rstrip()
    classroom_student = line.rstrip().split(";")

    while line:
        if line != "\n":
            classroom = classroom_student[2]
            students_in_room = 0

            print(classroom)
            while line and classroom_student[2] == classroom:
                students_in_room += 1
                print(f"\t{classroom_student[1]} {classroom_student[0]}")

                line = file.readline().rstrip()
                classroom_student = line.rstrip().split(";")
            print(f"Number of students in classroom {classroom} = {students_in_room}")
