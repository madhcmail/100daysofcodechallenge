from datetime import datetime
from datetime import date

# prints today date and time as
# 2020-04-19 18:37:02.765391
today = datetime.today()
print(today)

# prints just today's date
# 2020-04-19
today_date = date.today()
print(today_date)

print(today_date.day)
print(today_date.month)
print(today_date.year)

hundred_days_from_today = datetime(2020, 7, 29, 18, 37, 2, 765391)

# checks whether the final date falls on July 29th or not
check_accuracy = hundred_days_from_today - today
print(type(check_accuracy))
if check_accuracy.days == 100:
    print("yay! my 100th day challenge is on July 29th 2020")
    print(check_accuracy.days)
else:
    print("No! check your date")
    print(check_accuracy.days)

today = datetime.today()
print(today)
time_in_seconds = datetime.today().second
print(time_in_seconds)
time_in_minutes = datetime.today().minute
print(time_in_minutes)

# convert string  to datetime object
line = "2020-04-03T23:27:51"
convert_line_datetime = datetime.fromisoformat(line)
print(convert_line_datetime)
