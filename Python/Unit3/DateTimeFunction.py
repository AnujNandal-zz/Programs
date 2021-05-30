from datetime import date
import datetime
import time

date_object = datetime.datetime.now()
print(date_object)

date_object = datetime.date.today()
print(date_object)

print(date_object.year)

print(date_object.strftime("%A"))

timestamp = date.fromtimestamp(1616244364)
print("Date = ", timestamp)

# print(dir(datetime))

localtime = time.localtime(time.time())
print("Local current time :", localtime)
