principal = 1000 
rate = 0.07      
year = 1          
print("Year\tAmount on deposit")

while year <= 30:
    amount = principal * (1 + rate) ** year
    print(year, "\t", round(amount))
    year = year + 1
