def first_value(x):
    return x[0] > 2

tuples = [(1, 'A'), (4, 'B'), (2, 'C')]
filtered = list(filter(first_value, tuples))
