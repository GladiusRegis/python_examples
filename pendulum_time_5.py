import pendulum

dt = pendulum.now()
print(dt.format('dddd DD MMMM YYYY', locale='pl'))
