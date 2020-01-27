'''
https://www.youtube.com/watch?v=jxmzY9soFXg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=53
Logging Advanced - Loggers, Handlers, and Formatters
'''
import logging
import Employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(stream_handler)  # display the logs in console as well

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    try:
        result =  x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result

num_1 = 20
num_2 = 0

add_result = add(num_1,num_2)
logger.debug('Add : {} + {} = {} '.format(num_1,num_2,add_result))
sub_result = sub(num_1,num_2)
logger.debug('Sub : {} - {} = {} '.format(num_1,num_2,sub_result))
mul_result = mul(num_1,num_2)
logger.debug('Mul : {} * {} = {} '.format(num_1,num_2,mul_result))
div_result = div(num_1,num_2)
logger.debug('Div : {} / {} = {} '.format(num_1,num_2,div_result))
print('\n')
