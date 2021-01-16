#  Jonas Claes <r0841639@student.thomasmore.be>

def remove_vowels(text: str):
    vowels = ("A", "E", "I", "O", "U")
    for vowel in vowels:
        text = text.replace(vowel, "")
        text = text.replace(vowel.lower(), "")
    return text


with open("hamlet2.txt") as input_file:
    with open("hamlet3.txt", "w") as output_file:
        input_characters = 0
        output_characters = 0
        line = input_file.readline()
        while line:
            input_characters += len(line)
            no_vowels_line = remove_vowels(line)
            output_characters += len(no_vowels_line)
            output_file.write(no_vowels_line)
            line = input_file.readline()

    print(f"The input file contains {input_characters} characters")
    print(f"The output file contains {output_characters} characters")
