# x = 99

# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)


# x = 99

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     f2()
# f1()

def chaipani(num):
    def actual(x):
        return x ** num
    return actual



f = chaipani(2)
g = chaipani(3)

print(f(3))
print(g(3))