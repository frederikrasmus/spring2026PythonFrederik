import os

#1
os.mkdir('os_exercises.')
#2
os.chdir('os_exercises')
open('exercise.py', 'w')
#3
x = input('Please write something to the file: ')
with open('exercise.py', 'w') as f:
    f.write(x)

#4 
x = input('Please write something More to anoter file: ') 
with open('exercise2.py', 'w') as f:
    f.write(x)

#5
with open('exercise.py', 'r') as f1:
    with open('exercise2.py', 'r' ) as f2:
        print(f1.read() + f2.read())

