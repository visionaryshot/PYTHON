def is_even(x):
    return x % 2 == 0

even_numbers = list(filter(is_even, range(1, 21)))
