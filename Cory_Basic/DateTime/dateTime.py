'''
https://www.youtube.com/watch?v=eirjjyP2qcQ
Datetime Module - How to work with Dates, Times, Timedeltas, and Timezones

pip install pytz- standard lib for time zone
'''
import datetime

'''
example of date
'''
d = datetime.date(2019,4,10)
# print(d)

tday =datetime.date.today()
# print(tday)
# print(tday.year)
# print(tday.day)
# print(tday.month)
# #Monday is 0 sunday is 6
# print(tday.weekday())
# #iso weekday - Monday is 1 sunday is 7
# print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)
# print(tdelta)
# print('\n')
# print(tday + tdelta)  # prints 7 days from the current day
# print(tday - tdelta)  #prints what was day one week ago

# calculation of number of days till my birthday
# bday = datetime.date(2019,8,20)
# till_bday = bday - tday
# print(till_bday)
# print(till_bday.days)
# print(till_bday.total_seconds())

print('\n')

'''
example of time
'''
# t = datetime.time(9, 30, 45, 100000)
# print(t)
# print(t.hour)

'''the datetime.datetime commonly used as it displayes both'''
d = datetime.date(2019,4,10)
t = datetime.time(9, 30, 45, 100000)
dt = datetime.datetime(2019,4,10,9, 30, 45, 100000 )
print(d)
print(t)
print(dt)
print(dt.date())
print(dt.time())
tdeltdt = datetime.timedelta(days=7)
print(dt+tdeltdt)
tdelttime = datetime.timedelta(hours=12)
print(dt+tdelttime)
print('\n')

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utc = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utc)
