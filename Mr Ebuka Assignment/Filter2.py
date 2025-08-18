def long_numbers(word):
    return len(word) > 5

words = ['cat', 'elephant', 'tiger', 'lion']
long_words = list(filter(long_numbers, words))
