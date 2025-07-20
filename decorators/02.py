def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f'{key}={value}' for key, value in kwargs.items())
        return func(*args, **kwargs)
    
    return wrapper






def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet("chai", greeting="Hi")