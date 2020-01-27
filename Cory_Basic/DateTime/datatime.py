# https://www.youtube.com/watch?v=eirjjyP2qcQ&index=24&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
'''
Python Tutorial: Datetime Module - How to work with Dates, Times, Timedeltas, and Timezones
'''
import datetime
import pytz

dt = datetime.date(2016, 1,13)
print('date  is :\t', dt)

tday = datetime.date.today()
print('Today date  is :\t', tday)

#date format
tday = datetime.date.today()
print('Today date  is :\t', tday.day)
print('Today date  is :\t', tday.month)
print('Today date  is :\t', tday.year)
print(tday.weekday())  # weekday  - monday is 0 and sunday is 6
print(tday.isoweekday()) # iso weekday - monday is 1 and sunday is 7



#time deltas
tdelta = datetime.timedelta(days=7)
print('date after one week from the today  is : \t',tday+tdelta)  # tells us date from current date to 7 days
print('date before one week from the today  is : \t',tday-tdelta)
print(tday-tdelta)
print(tday+tdelta)
print("\n")
#calculate birthday
bday = datetime.date(2019, 8, 25)
till_bdy= bday-tday
print('there are '+ str(till_bdy.days) + ' remaining to celebrate your birthday')
print('there are '+ str(till_bdy.total_seconds()) + ' seconds remaining to celebrate your birthday')
print("\n")

#time format
dtm = datetime.time(11,18,45,100000)
print('time is : \t',dtm)
print('hour is : \t',dtm.hour)
print('second is : \t',dtm.minute)
print('minute is : \t',dtm.second)
print('microseconds is : \t',dtm.microsecond)
print("\n")

#date and time format
tdeltahr = datetime.timedelta(hours=12)
tdtm = datetime.datetime(2019,1,13,11,22,45,100000)
print('date and time is : \t',tdtm)
print('date  is : \t',tdtm.date())
print('time  is : \t',tdtm.time())
print('date and time delta is : \t',tdtm+tdelta)
print('date and time delta is : \t',tdtm+tdeltahr)
print("\n")

# date format today now and utc

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utc = datetime.datetime.utcnow()

print('today date is     : \t',dt_today)
print('today date now is : \t',dt_now)
print('UTC date is       : \t',dt_utc)
print("\n")

# working using pytz
dt = datetime.datetime(2019,1,14,8,46,25,tzinfo=pytz.UTC )
print(dt)

#two way of get current UTC time
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print('UTC date is       : \t',dt_utcnow)
dt_utc1 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print('UTC date is       : \t',dt_utc1)
print("\n")

#converting different zone time using UTC time now

dt_mtn =dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print('US Mountain time now (MTS)           : \t',dt_mtn)

dt_est =dt_utcnow.astimezone(pytz.timezone('US/Eastern'))
print('US Mountain time now (EST)           : \t',dt_est)
# convert iso format which is std format
print('US Mountain time now (MTS ISO format): \t',dt_mtn.isoformat())
# general format strftime - convert from datetime int string
print('US Eatern time now (normal format)    : \t',dt_est.strftime('%B %d, %Y' ))
dt_str = dt_est.strftime('%B %d, %Y' )
# convert normal format to generic format -strptime() - convert from string to datetime
print('US Eatern time now (normal format)    : \t',datetime.datetime.strptime(dt_str,'%B %d, %Y'))
print("\n")


#to print all time zone in the worl

for tz in pytz.all_timezones:
    # print(tz)
    all_zonetime=dt_utcnow.astimezone(pytz.timezone(tz))
    print(tz +'  -  '+str(all_zonetime))
print("\n")


