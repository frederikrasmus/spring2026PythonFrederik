# school_of_students.py

import random
import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        val = func(*args)
        end = (time.time()) - start
        print(f'Time elepsed: {end}')
        return val
    return wrapper

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

@timer
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    # return result

@timer
def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person













