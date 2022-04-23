from datetime import datetime, timedelta

start = input('Start of work, dd.mm.yyyy: ')
end = input('End date of work, dd.mm.yyyy: ')
wage = float(input('Daily rate: '))

date_start = datetime.strptime(start, '%d.%m.%Y')
date_end = datetime.strptime(end, '%d.%m.%Y')

diff = (date_end - date_start).days

working_days = diff
project_day = date_start

for _ in range(0, working_days + 1):
    if project_day.strftime('%a') in ['Sat', 'Sun']:
        working_days += 1
    print(f'You work on {project_day.strftime("%a, %d.%m.%Y")}')
    project_day += timedelta(days=1)

print(f'Salary: {working_days * wage}')


