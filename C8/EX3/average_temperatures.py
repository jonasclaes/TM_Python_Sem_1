#  Jonas Claes <r0841639@student.thomasmore.be>
with open("../files/weather_2018 10.csv") as file:
    # Strip the header of the file
    file.readline()

    line = file.readline().rstrip()
    weather_data_row = line.split(";")

    print("Average temperatures:")
    while line:
        if line != "\n":
            end_pos_date = weather_data_row[0].find(" ")
            date = weather_data_row[0][:end_pos_date]
            number_of_measurements = 0
            total_sum_temperatures = 0

            while line and weather_data_row[0][:weather_data_row[0].find(" ")] == date:
                number_of_measurements += 1
                total_sum_temperatures += float(weather_data_row[1])

                line = file.readline().rstrip()
                weather_data_row = line.split(";")
            average = total_sum_temperatures / number_of_measurements
            average = round(average * 100) / 100
            print(f"{date}\tnumber of measurements = {number_of_measurements}\taverage={average}")
    print(">"*58)
