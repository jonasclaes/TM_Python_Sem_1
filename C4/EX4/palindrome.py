word = input("Enter a word: ")

correct_chars = 0
for i in range(0, len(word)):
    if word[i] == word[-i - 1]:
        correct_chars += 1

if correct_chars == len(word):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
