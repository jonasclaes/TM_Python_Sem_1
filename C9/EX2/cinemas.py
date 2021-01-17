#  Jonas Claes <r0841639@student.thomasmore.be>
import xml.etree.ElementTree as ET

# Read XML file and get root element
xmlDoc = ET.parse("../files/cinemas.xml")
root = xmlDoc.getroot()

print("Bioscopen in Antwerpen")
for cinema in root.findall("bioscoopoverzicht"):
    cinema_name = cinema.find("naam").text
    cinema_street = cinema.find("straat").text
    cinema_street_number = cinema.find("huisnummer").text
    cinema_postal_code = cinema.find("postcode").text
    cinema_district = cinema.find("district").text

    # Format:
    # CINEMA_NAME
    # CINEMA_STREET CINEMA_STREET_NUMBER
    # CINEMA_POSTAL_CODE CINEMA_DISTRICT
    print(f"{cinema_name}")
    print(f"{cinema_street} {cinema_street_number}")
    print(f"{cinema_postal_code} {cinema_district}")
    print()
