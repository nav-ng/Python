import datetime

# mydate = datetime.date(1996, 12, 11)
# print(mydate)


tday = datetime.date.today()
print("Today's date is", tday)


# tday = datetime.date.today()
# print("Current year", tday.year)
# print("Current year", tday.month)
# print("Current year", tday.day)


# now(): to display the current date and time


# tday=datetime.datetime.now()
# print("Current date and time is", tday)


# find the difference between two days
# import datetime

# date1 = datetime.datetime(2022, 11, 1)
# date2 = datetime.datetime(2022, 2, 4)
# diff = date1 - date2
# print("Difference is ", diff)


# timedelta(): the timedelta class is used for calculating difference between dates and represents the duration.


from datetime import timedelta
#
date = datetime.date.today()
date += timedelta(days=100)
print("date after 100 days is", date)


# from datetime import timedelta
#
# date = datetime.date.today()
# date -= timedelta(days=100)
# print("date before 100 days is", date)
