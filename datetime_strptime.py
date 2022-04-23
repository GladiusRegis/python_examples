from datetime import datetime

birthday = input('Enter your date of birth dd.mm.yyyy: ')
d = datetime.strptime(birthday, '%d.%m.%Y')

print(d)
