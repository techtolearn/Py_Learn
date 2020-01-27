# https://www.youtube.com/watch?v=KlBPCzcQNU8&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=38
'''
Python Tutorial: Decorators With Arguments
'''


def prefix_decorator(prefix):
    def decorator_function(original_fun):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed Before',original_fun.__name__)
            result = original_fun(*args,**kwargs)
            print(prefix, 'Executed After',original_fun.__name__)
            return  result
        return wrapper_function
    return decorator_function

@prefix_decorator('Testing : ')
def display_info(name,age):
    print('Display_info ran with arguments ({}, {})'.format(name,age))


display_info('Satheesh',38)
print('\n')
display_info('Divya',36)
