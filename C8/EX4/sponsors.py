#  Jonas Claes <r0841639@student.thomasmore.be>
with open("../files/sponsors.txt") as file:
    line = file.readline()

    sponsors = {}
    while line:
        if line != "\n":
            sponsor = line.rstrip().split("*")
            sponsor_id = int(sponsor[0])

            if not sponsors.get(sponsor_id):
                first_name = sponsor[1]
                last_name = sponsor[2]
                sponsors[sponsor_id] = [sponsor_id, first_name, last_name, 0]

            sponsors[sponsor_id][3] += int(sponsor[3])

        line = file.readline()

    print("Overview gifts")
    print("Number\tSponsor")
    amount_of_tax_certificates = 0
    for sponsor_id in sorted(sponsors):
        sponsor = sponsors[sponsor_id]
        print(f"{sponsor_id}\t{sponsor[1]} {sponsor[2]}\t{sponsor[3]}", end="")

        if sponsor[3] >= 40:
            print("\t**")
            amount_of_tax_certificates += 1
        else:
            print()
    print(f"There are {amount_of_tax_certificates} tax certificates to be sent.")
