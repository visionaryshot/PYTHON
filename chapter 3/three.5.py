
"""Comparing integers using if statements and comparison operators."""
print('Enter two integers, and I will tell you',
      'the relationships they satisfy.')

num1 = int(input('Enter first integer: '))

num2 = int(input('Enter second integer: '))

if num1 == num2:
    print(num1, 'is equal to', num2)
else:
    print(num1, 'is not equal to', num2)

if num1 < num2:
    print(num1, 'is less than', num2)
else:
    print(num1, 'is greater than or equal to', num2)

if num1 > num2:
    print(num1, 'is greater than', num2)
else:
    print(num1, 'is less than or equal to', num2)