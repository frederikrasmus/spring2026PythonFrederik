# os_exercise.py
# Do the following task using the os module

"""
1. create a folder and name the folder 'os_exercises.'                                                  
2. In that folder create a file. Name the file 'exercise.py'                                                                            
3. get input from the console and write it to the file.                                                 
4. repeat step 2 and 3 (name the file something else).                                                  
5. read the content of the files and and print to console the content of the file with the largest amount of unique words.
"""

import os

# 1

if os.path.isdir('os_exercises'):
    pass
else:
    os.mkdir('os_exercises')


# 2
os.chdir('os_exercises')

for i in range(1, 4):

    f = open(f'exercise_{i}.py', 'w')

    
    # 3
    j = input('Please write somthing')
    f.write(j)
    
    f.close()
    


def unique_words(f):
    t = f.read()
    t = t.split()
    t = set(t)
    return len(t)


print(unique_words(open('exercise_1.py')))
print(unique_words(open('exercise_2.py')))
print(unique_words(open('exercise_3.py')))



os.listdir('.')


















