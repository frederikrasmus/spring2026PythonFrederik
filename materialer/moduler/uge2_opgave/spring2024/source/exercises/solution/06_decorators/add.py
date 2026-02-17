# add.py

import datetime

def log(func):
    def wrapper(*args):
        f = open('log.txt', 'a+')
        f.write(f'{datetime.datetime.now()}, {args}, {func(*args)}\n')
        return func(*args)
    return wrapper

@log
def add(*args):
    sum = 0
    for i in args:
        sum += i 
    return sum

@log
def printer(text):
    print('From printer')
