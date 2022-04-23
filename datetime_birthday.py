from datetime import date
"""Birthday"""

birthday_day = int(input("Enter the day of birth: "))
birthday_month = int(input("Ender the month of birth: "))
today = date.today()
birthday = date(today.year, birthday_month, birthday_day)


if today > birthday:
    birthday = date(today.year + 1, birthday_month, birthday_day)

diff = birthday - today
print(f'In {diff.days} days on {birthday.strftime("%A")} it will be your birthday ')
