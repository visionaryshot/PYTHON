def capitalize_name(name):
    return name.capitalize()

names = ['john', 'mary', 'steve']
capitalized = list(map(capitalize_name, names))
