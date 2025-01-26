import pandas as pd


time = pd.Timestamp(year=2025,month=1,day=26, hour=10)
print(time)

print("day of the week is ",time.dayofweek)

print("Day of the year",time.dayofyear)

print("Days in Month ",time.daysinmonth)

print("Is Leap year",time.is_leap_year)

print("Is this the last day of the month? ",time.is_month_end)