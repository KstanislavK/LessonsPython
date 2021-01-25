from functools import reduce
def my_f(a, b):
    return a * b
print(reduce(my_f, [i for i in range(100, 1001) if i % 2 == 0]))