REGISTER = []

def register(func):
    REGISTER.append(func)
    return func

# this functions simulate html pages
@register
def home():
    return 'Im the home page'

@register
def about():
    return 'Im the about page'

def excluded_for_now():
    return 'excluded'


# simple menu demo 
def menu():
    for i in enumerate(REGISTER):
        print( f'{i[1].__name__}' , end=' ')
    print()

choise = False

while True: 
    menu()
    if choise:
        choise = REGISTER[choise - 1]()
        print(choise)
    choise = int(input('choose a number: '))




