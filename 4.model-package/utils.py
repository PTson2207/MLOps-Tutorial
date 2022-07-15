import time
from functools import wraps

def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print('{} took {:.2f} seconds'.format(f.__name__, end - start))
        return result
    
    return wrapper