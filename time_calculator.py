"""Converting a time given only in seconds to a time in hours: minutes: seconds."""

time = int(input("Enter time in seconds (s): \n"))

minutes = time // 60
second = time % 60
hours = minutes // 60
minutes_h = minutes % 60

if hours == 0:
    minutes_time = minutes
    seconds_time = second
    print(f'This is {minutes_time} minutes and {seconds_time} seconds')
elif hours != 0:
    hours_time = hours
    minutes_time = minutes_h
    seconds_time = second
    print(f'This is {hours_time} hours, {minutes_time} minutes and {seconds_time} seconds')
else:
    print('Enter the correct value for seconds.')


