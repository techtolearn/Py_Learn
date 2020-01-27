
# https://www.youtube.com/watch?v=FsAPt_9Bf3U&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=37
'''
Decorators - using logging function
'''
import os
def my_logger(org_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(org_func.__name__), level=logging.INFO)  # log file will generate in root dir

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args,kwargs))
        return org_func(*args, **kwargs)
    return wrapper


def my_timer(org_func):
    import time

    def wrapper(*args, **kwargs):
        t1 =time.time()
        result = org_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in : {} sec'.format(org_func.__name__, t2))
        return  result
    return  wrapper

import time
@my_logger
@my_timer
def display_info(name,age):
    time.sleep(1)
    print("Display information of the persion : name:{} and age:{} ".format(name,age))

display_info('Satheesh',38)
