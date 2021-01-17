#  Jonas Claes <r0841639@student.thomasmore.be>
import xml.etree.ElementTree as ET

xmlDoc = ET.parse("../files/drugs.xml")
root = xmlDoc.getroot()

for leaflet in root.iter("leaflet"):
    pharmaceutical_forms = leaflet.find("pharmaceutical_forms")
    name = leaflet.find("name")

    leaflet.remove(pharmaceutical_forms)
    name.text = name.text.upper()

xmlDoc.write("drugs_changed.xml", encoding="UTF-8", xml_declaration=True)
