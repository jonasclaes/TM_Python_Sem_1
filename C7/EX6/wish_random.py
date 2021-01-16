#  Jonas Claes <r0841639@student.thomasmore.be>
import random

wish_number = random.randint(1, 10)
print(f"Wish {wish_number}\n")
with open(f"../files/wish{wish_number}.txt") as file:
    print(file.read(), end="")
