# Get current hour and time to wait
current_hour = int(input("Enter the current hour: "))
wait_time = int(input("Enter the time you want to wait: "))

sound_time = (current_hour + wait_time) % 24

print("The alarm will sound at " + str(sound_time) + "h.")
