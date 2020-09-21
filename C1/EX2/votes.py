# Get votes
votes_yes = int(input("How many people voted YES: "))
votes_no = int(input("How many people voted NO: "))
votes_blank = int(input("Number of blank votes: "))

# Calculate total and percentages
votes_total = votes_yes + votes_no + votes_blank
votes_yes_percentage = (votes_yes / votes_total) * 100
votes_no_percentage = (votes_no / votes_total) * 100
votes_blank_percentage =(votes_blank / votes_total) * 100

print("YES: " + str(votes_yes_percentage) + "%")
print("NO: " + str(votes_no_percentage) + "%")
print("Blank: " + str(votes_blank_percentage) + "%")