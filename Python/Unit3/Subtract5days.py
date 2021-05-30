import datetime
a_date = datetime.date(2021, 5, 19)

days = datetime.timedelta(5)

new_date = a_date - days
print(new_date)
