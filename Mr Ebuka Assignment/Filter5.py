def  palindrome(word):
    return word == word[::-1]

words = ['level', 'world', 'madam', 'python']
palindromes = list(filter(palindrome, words))
