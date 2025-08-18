def get_tax(price):
    return price * 1.10

prices = [100, 200, 300]
tax = list(map(get_tax, prices))
