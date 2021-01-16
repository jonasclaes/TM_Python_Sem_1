#  Jonas Claes <r0841639@student.thomasmore.be>
with open("../files/books.txt") as file:
    count = 1
    book = file.readline()
    while book:
        author = file.readline()
        print(f"{count}. {book.rstrip()} -> {author.rstrip()}")

        book = file.readline()
        count += 1
