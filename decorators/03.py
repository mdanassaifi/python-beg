import time

def cache(func):
    cache_value = {}
    def wrapper(*args):
        result = func(*args)
        return result
    return wrapper







def long_running_function():
    time.sleep(4)
    return a + b