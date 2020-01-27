import  datetime

current_weight = 220
goal_weight = 180
avg_lbs_week = 1.5

start_date = datetime.date.today()
end_date =start_date
while goal_weight < current_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= avg_lbs_week
print(end_date)
print(f'Reached goal in {(end_date-start_date).days // 7 }.weeks')
