import datetime
import math

goals_sub = 100000
current_sub = 85000

subs_to_go = goals_sub - current_sub

avg_subs_day =200

days_to_go = math.ceil(subs_to_go/avg_subs_day)
today = datetime.date.today()
goal= today + datetime.timedelta(days=days_to_go)
print(goal)
