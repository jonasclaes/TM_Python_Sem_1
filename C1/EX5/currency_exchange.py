# Get exchange rate
exchange_rate = float(input("Enter the current EUR <-> DOLLAR rate: "))
amount_in_euro = float(input("Amount in EUR: "))

# Print exchanged rate
print(str(amount_in_euro) + " € = " + str(amount_in_euro * exchange_rate) + " $")
