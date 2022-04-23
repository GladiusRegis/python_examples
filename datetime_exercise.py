from datetime import datetime, timedelta

start = input('Start of work, dd.mm.yyyy: ')
end = input('End date of work, dd.mm.yyyy: ')
wage = float(input('Daily rate: '))

date_start = datetime.strptime(start, '%d.%m.%Y')
date_end = datetime.strptime(end, '%d.%m.%Y')

diff = (date_end - date_start).days

print(f'Salary: {diff * wage}')

for _ in range(0, diff):
    project_day = date_start + timedelta(days=1)
    print(f'You are working on {project_day.strftime("%a, %d.%m.%Y")}')


#
# while counter <= numbers_days:
#     day_week = (d_start + timedelta(days=counter))
#     print(day_week)
#     week = day_week.weekday()
#     print(week)
#     counter += 1
#     if week in [0, 6]:
#         holideys += daily_rate
#
# salary_total = salary + holideys * daily_rate
# print(salary_total)
#


