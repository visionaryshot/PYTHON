number = int(input('Enter a five-digit integer: '))
num1 = number // 10000
num2 = (number % 10000) // 1000
num3 = (number % 1000) // 100
num4 = (number % 100) // 10
num5 = number % 10

print(num1, "   ", num2, "   ", num3, "   ", num4, "   ", num5)