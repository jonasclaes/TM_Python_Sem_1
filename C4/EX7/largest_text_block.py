text = input("Enter a text: ")

largest_block = 1
for char in text:
    if text.count(char) > largest_block:
        largest_block = text.count(char)

print("The length of the largest block in this text is", largest_block)
