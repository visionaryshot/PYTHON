def divide(x):
    return x % 3 == 0 and x % 5 == 0

divisible = list(filter(divide, range(1, 51)))
