power_consumption_day = int(input("Power consumption during the day (kWh): "))
power_consumption_night = int(input("Power consumption during the night (kWh): "))

fixed_costs = 83.6
tariff_day = 0.068
tariff_night = 0.035
consumption_daily = tariff_day * power_consumption_day
consumption_nightly = tariff_night * power_consumption_night
total_excluding_vat = fixed_costs + consumption_daily + consumption_nightly
total_including_vat = total_excluding_vat * 1.21

print("Invoice")
print("*" * 7)
print("Fixed costs: € " + str(fixed_costs))
print("Daily consumption: € " + str(consumption_daily))
print("Nightly consumption: € " + str(consumption_nightly))
print("Total excluding VAT: € " + str(total_excluding_vat))
print("Total including VAT: € " + str(total_including_vat))
