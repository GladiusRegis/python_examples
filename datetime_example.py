from datetime import date, timedelta

today = date.today()
print(f'Today is : {today}')

formatted = today.strftime("%d.%m.%Y")
print(formatted)

day = date(today.year, 1, 11)

print(f'My birthday {day} ')


"""Birthday"""

today = date.today()
birthday = date(today.year, 1, 11)

if birthday > today:
    diff = birthday - today
    print(f'In {diff.days} days it will be your birthday ')
else:
    diff = today - birthday
    print(f'Birthday was {diff.days} days ago')

