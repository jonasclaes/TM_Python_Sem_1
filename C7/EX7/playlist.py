#  Jonas Claes <r0841639@student.thomasmore.be>
print("Playlist")
with open("../files/playlist.txt") as file:
    playlist = file.readlines()
    playlist.reverse()
    for row in playlist:
        if row != "\n":
            columns = row.split(";")
            time = columns[0].rstrip()
            song = columns[1].rstrip()
            author = columns[2].rstrip().lower()
            print(f"{time}\t{song} ({author})")
