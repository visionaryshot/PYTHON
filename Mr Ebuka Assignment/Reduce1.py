from functools import reduce

def add(x, y):
    return x + y

sum = reduce(add, range(1, 51))
print(sum) 
