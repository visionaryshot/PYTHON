def square(x):
    return x ** 2

def multiply(x, y):
    return x * y

squares = map(square, [1, 2, 3, 4])
product = reduce(multiply, squares)
print(product) 
