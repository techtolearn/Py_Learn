'''
https://www.youtube.com/watch?v=5iWhQWVXosU&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=54
Python Quick Tip: Hiding Passwords and Secret Keys in Environment Variables (Mac & Linux)
https://www.youtube.com/watch?v=IolxqkL7cD8&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=55
Python Quick Tip: Hiding Passwords and Secret Keys in Environment Variables (Windows)

Set username and password in environment user var setting and access here and write the below code and restart the editor
'''

import os

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')

print('User Name is  : ',db_user)
print('Password  is  : ',db_password)
