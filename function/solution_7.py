def sum_all(*args):
    """Returns the sum of all arguments."""
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)
    
print(sum_all(1, 2, 3))