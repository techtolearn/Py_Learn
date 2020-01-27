# # https://www.youtube.com/watch?v=bD05uGo_sVI&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=36
# '''
# Generators - How to use them and the benefits you receive
# Generator will not hold any value while printing hence it is good for performance - it is just holding current value from the loop
# '''

import memory_profiler
import random
import time

name = ['John','Corey','Adam','Stev','Rick','Thomas']
majors = ['Math','Science','History','Computer','Geography','Business']

print ('Memory (Before holding records) :  {}MB'.format(memory_profiler.memory_usage()))

# this will consume more memory when we use list for holding 1000000 records
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = { 'id': 'i',
                   'name': random.choice(name),
                   'major': random.choice(majors)
                }
        result.append(person)
    return result


def people_generator(num_people):
     for i in range(num_people):
        person = { 'id': 'i',
                   'name': random.choice(name),
                   'major': random.choice(majors)
                }
        yield person


# t1 = time.process_time()
# people = people_list(1000000)
# t2 = time.process_time()
#
# print('Memory using List (After holding records) :  {} MB'.format(memory_profiler.memory_usage()))
# print('Took {} Seconds'.format(t2-t1))
# print('\n')

T1 = time.process_time()
peopleGen = people_generator(1000000)
T2 = time.process_time()


print('Memory using Generator (After holding records) :  {} MB'.format(memory_profiler.memory_usage()))
print('Took {} Seconds'.format(T2-T1))
