from datetime import date, timedelta, datetime

date_start = input('Start date of wokr, dd.mm.yyyy: ')
date_end = input('End date of wokr, dd.mm.yyyy: ')
daily_rate = int(input('Daily rate: '))

d_start = datetime.strptime(date_start, '%d.%m.%Y')
d_end = datetime.strptime(date_end, '%d.%m.%Y')
numbers_days = int((d_end - d_start).days)

salary = numbers_days * daily_rate
print(salary)

holideys = 0
counter = 0
while counter <= numbers_days:
    day_week = (d_start + timedelta(days=counter))
    print(day_week)
    week = day_week.weekday()
    print(week)
    counter += 1
    if week in [0, 6]:
        holideys += daily_rate

salary_total = salary + holideys * daily_rate
print(salary_total)



