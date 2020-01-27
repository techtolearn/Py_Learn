'''
https://www.youtube.com/watch?v=k8asfUbWbI4&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=48
Calculate Number of Days, Weeks, or Months to Reach Specific Goals
'''
import  datetime
import calendar

balance =5000
interest_rate = 13 * 0.1
monthly_payment = 500

today = datetime.date.today()
print(today.year,' ',today.month,' ',today.day)
days_in_Current_month =  calendar.monthrange(today.year, today.month)[1]  #it gives number of days for the current month
print(days_in_Current_month)
date_till_end_month = days_in_Current_month - today.day
print(date_till_end_month)
start_date = today + datetime.timedelta(days=date_till_end_month +1) #it will give begin of the next month - when you add it will give 31 days
end_date =start_date                                                               # since current month 30 days which is april,it will give may 01

while balance > 0:
    interest_charge = (interest_rate /12 ) * monthly_payment
    balance+=interest_charge;
    balance-=monthly_payment

    balance = round(balance,2)
    if balance < 0:
        balance = 0
    print(end_date,balance)
      #or balance = 0 if balance < 0 else  round(balance,2)

    date_till_current_month = calendar.monthrange(end_date.year,end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=date_till_current_month)

