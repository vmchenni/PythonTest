# Weather forecasting organization wants to show is it day or night. So,
# write a program for such organization to find
# whether is it dark outside or not.
# ANSWER
from datetime import datetime

now = datetime.now()
current_hour = int(now.strftime("%H"))
print("Current hour is:-", current_hour)
if current_hour > 19 and current_hour < 7:
    print("It is night")
else:
    print("It's Day time")