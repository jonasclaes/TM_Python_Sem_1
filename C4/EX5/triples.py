text = input("Enter a text: ")

triples = 0
position = 0
for char in text:
    if text[position:len(text)].count(char * 3) > 0:
        triples += 1
    position += 1

if triples == 0:
    print("There are no triples in this text.")
elif triples == 1:
    print("There is 1 triple in this text.")
elif triples > 1:
    print("There are {0} triples in this text.".format(triples))
