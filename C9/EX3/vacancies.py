#  Jonas Claes <r0841639@student.thomasmore.be>
import xml.etree.ElementTree as ET

xmlDoc = ET.parse("../files/jobs.xml")
root = xmlDoc.getroot()

print("Overview IT vacancies:\n")

count = 0
for company in root.iter("company"):
    company_name = company.find("name").text
    company_contact_email = company.find("contact").find("email").text

    for vacancy in company.iter("vacancy"):
        position = vacancy.find("position")
        if position.get("group") == "IT":
            count += 1
            print(f"{count}.\tPosition:\t{position.text}")
            print(f"\tCompany:\t{company_name}")
            print(f"\tContact:\t{company_contact_email}")
            print()
