# returntype.py

# All functions has a return type and value. If no one is specified, the function will return a value of 'None' which has the type of 'NoneType'.
# So a function like this:

def add():
    print('Hello')

# will in reality look like this:

def add():
    print('Hello')
    return None

# so it is important not to think that this function:

def add():
    print('Hello')

# has the return value of 'Hello'.
# It has a side effect of printing out 'Hello', but a return value of 'None'.
