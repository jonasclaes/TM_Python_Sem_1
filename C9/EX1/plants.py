#  Jonas Claes <r0841639@student.thomasmore.be>
import xml.etree.ElementTree as ET

# Read XML file and get root element
xmlDoc = ET.parse("../files/plants.xml")
root = xmlDoc.getroot()

count = 1
for plant in root.iter("plant"):
    plant_light = plant.find("light").text

    if plant_light == "SUN":
        plant_common_name = plant.find("common").text
        plant_botanical_name = plant.find("botanical").text
        print(f"Plant {count} : {plant_common_name} ({plant_botanical_name.capitalize()})")
        count += 1
