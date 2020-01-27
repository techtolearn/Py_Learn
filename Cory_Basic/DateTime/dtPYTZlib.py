import datetime
import pytz

# dt = datetime.datetime(2019,4,10,9, 30, 45, tzinfo=pytz.utc)
# print(dt)
dt_utcnow = datetime.datetime.now(tz=pytz.utc)
#print(dt_utcnow)
# dt_utc = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
# print(dt_utc)


# dt_mtn= dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)

#converting local time from utz time zone
# dt_mtn= datetime.datetime.now()
# mtn_tz= pytz.timezone('US/Mountain')
# dt_mtn=mtn_tz.localize(dt_mtn)
# print(dt_mtn)
# #finding eastern time
# dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)



'''
strftime = datetime to string
strpptime = string to datetime
'''
#
# dt_mtn = datetime.datetime.now(tz=pytz.timezone("US/Mountain"))
# print(dt_mtn.strftime('%B %d, %Y'))  #refer the python documention for codes
#
# dt_str = 'April 10, 2019'
# dt = datetime.datetime.strptime(dt_str,'%B %d, %Y')
# print(dt)


#get all time zone

for tz in pytz.all_timezones:
    print(tz)
