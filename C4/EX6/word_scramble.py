word = input("Enter a string: ")

constructed_string = ""
for i in range(0, len(word), 3):
    string = word[i:i+3]
    if len(string) == 3:
        constructed_string += string[1] + string[2] + string[0]
    else:
        constructed_string += string

print(constructed_string)
