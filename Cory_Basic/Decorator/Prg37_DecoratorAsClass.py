# https://www.youtube.com/watch?v=FsAPt_9Bf3U&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=37
'''
Decorators - Dynamically Alter The Functionality Of Your Functions
'''

# - getting an error for the below program - not sure
# Below example shows - how to define decorator as class
# example 5
print('Decorator as class')
print('******************')

def decorator_function(original_function):
        def wrapper_function(*args,**Kwargs):
            print('wrapper function executed this before {} function'.format(original_function.__name__))
            return original_function(*args,**Kwargs)  # return as a function
        return wrapper_function

class decorator_class(object):

    def __int__(self,original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('Call method executed this before {} function'.format(self.original_function.__name__))
        return self.original_function(*args,**kwargs)

@decorator_class
def display():
    print("we no need to call decorator function here instead just call display function")

@decorator_class
def display_info(name,age):
    print("Display information of the person : name:{} and age:{} ".format(name,age))

display_info('Adam',38)
display()
