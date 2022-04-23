from datetime import date

start = int(input("From what year do you want to check the day of the week of birth: "))
end = int(input("To what year do you want to check the day of the birth week:"))

for year in range(start, end):
    birthday = date(year, 1, 11)
    print(f'Birthday in {birthday.strftime("%Y is %A")}')
