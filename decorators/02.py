def debug(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper






def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet("chai", greeting="Hi")