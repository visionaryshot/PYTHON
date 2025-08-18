def concat(x, y):
    return x + ' ' + y

sentence = reduce(concat, ['I', 'love', 'Python'])
print(sentence) 
