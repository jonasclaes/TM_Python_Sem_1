#  Jonas Claes <r0841639@student.thomasmore.be>
with open("../files/courses.csv") as input_file:
    with open("students.csv", "w", encoding="UTF-8") as output_file:
        # Strip the header of the file
        input_file.readline()

        line = input_file.readline().rstrip()
        course_student = line.split(";")

        while line:
            if line != "\n":
                student_number = course_student[3]
                last_name = course_student[4]
                first_name = course_student[5]

                output_file.write(f"{student_number};{last_name};{first_name}")
                while line and course_student[3] == student_number:
                    course_name = course_student[1]
                    student_group = course_student[2]
                    output_file.write(f";{course_name} ({student_group})")

                    line = input_file.readline().rstrip()
                    course_student = line.split(";")
                output_file.write("\n")
