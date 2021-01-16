#  Jonas Claes <r0841639@student.thomasmore.be>
from random import randint

random_number = randint(1, 10)
with open(f"../files/table_{random_number}.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"{i}x{random_number}={i*random_number}")
        if i != 10:
            file.write("\n")
