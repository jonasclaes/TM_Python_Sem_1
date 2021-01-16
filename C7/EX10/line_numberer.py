#  Jonas Claes <r0841639@student.thomasmore.be>
from os.path import exists

source_file_location = input("Source file location: ")
destination_file_location = input("Destination file location: ")
if exists(source_file_location):
    with open(source_file_location) as input_file:
        with open(destination_file_location, "w") as output_file:
            lines = input_file.readlines()
            count = 1
            for line in lines:
                output_file.write(f"{str(count).rjust(4)} {line.rstrip()}\n")
                count += 1
