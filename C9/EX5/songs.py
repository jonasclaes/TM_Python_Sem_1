#  Jonas Claes <r0841639@student.thomasmore.be>
import xml.etree.ElementTree as ET

with open("../files/songs.txt") as file:
    root = ET.Element("compilation")

    line = file.readline()

    while line:
        if line != "\n":
            record = line.rstrip().split(";")
            track = ET.Element("track")
            artist = ET.SubElement(track, "artist")
            artist.text = record[0]
            song = ET.SubElement(track, "song")
            song.text = record[1]

            root.append(track)

        line = file.readline()

    tree = ET.ElementTree(root)
    tree.write("songs.xml", encoding="utf-8", xml_declaration=True)
