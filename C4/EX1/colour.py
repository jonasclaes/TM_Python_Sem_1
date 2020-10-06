colour = input("What is your favourite colour: ")
print(colour[0] + colour[2])
print("This colour consists of {0} letters".format(len(colour)))
print()

for char in colour:
    print("{0} = {1}".format(char, ord(char)))

print()

count = 0
while count != len(colour):
    if count % 2:
        print("**{0}**".format(colour[count]))
    else:
        print("#{0}#".format(colour[count]))
    count += 1
