price = int(input("Enter purchase price in cents: "))
change = 100 - price

print("Your change is:")

quarters = change // 25
change = change % 25
print(quarters, "quarters")

dimes = change // 10
change = change % 10
print(dimes, "dimes")

nickels = change // 5
change = change % 5
print(nickels, "nickels")

print(change, "pennies")
