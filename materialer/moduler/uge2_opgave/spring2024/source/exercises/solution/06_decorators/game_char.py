def sharpshooter(func):
    def wrapper(*args):
        return f'{func(*args)} the sharpshooter'
    return wrapper

def stealthy(func):
    def wrapper(*args):
        return f'{func(*args)} and the stealthy character'
    return wrapper

@stealthy
@sharpshooter
def player():
    return "I'm the player character"

print(player())
