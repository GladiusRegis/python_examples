from datetime import date, timedelta

"""timedelta"""
start = date.today()
diff = timedelta(days=7)
end = start + diff
print(end.strftime('%d.%m.%y'))


from datetime import datetime

"""datatime"""
event = datetime.now()
print(event.hour)
print(event.minute)
print(event.strftime('%H:%M'))
