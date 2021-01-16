#  Jonas Claes <r0841639@student.thomasmore.be>
with open("../files/weather_2018 08.csv") as file:
    weather_data = file.readlines()
    # Remove off header
    weather_data = weather_data[1:]

    columns = weather_data[0].rstrip().split(";")
    highest_temperature = columns[1]

    for weather_data_point in weather_data:
        if weather_data_point != "\n":
            columns = weather_data_point.rstrip().split(";")
            if columns[1] > highest_temperature:
                highest_temperature = columns[1]

    print(f"The highest temperature in this period = {highest_temperature} degrees celsius")
