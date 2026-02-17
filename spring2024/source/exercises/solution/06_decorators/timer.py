# timer.py
import time

def timer(func):                                                                                                                                   
    def wrapper(*args, **kwargs):                                                                                                                  
        start = time.time()                                                                                                                        
        func(*args, **kwargs)                                                                                                                      
        end = (time.time()) - start                                                                                                              
        print(f'Time elapsed: {end}')                                                                                                              

    return wrapper                                                                                                                                 


@timer                                                                                                                                             
def genrate_list(num):                                                                                                                             
    [x for x in range(1, num)]
