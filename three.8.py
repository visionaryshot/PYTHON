count = 0
addition = 0
product = 1
smallest = None
largest = None

while count < 3:
    number = int(input('Enter any number:'))
    addition = addition + number
    product = product * number

    if count == 0:
        smallest = number
        largest = number
    else:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

    count = count + 1

average = addition / 3

print('Sum is', addition)
print('Average is', average)
print('Product is', product)
print('Smallest is', smallest)
print('Largest is', largest)








#number1 = int(input("Enter first number: "))
#number2 = int(input("Enter second number: "))
#number3 = int(input("Enter third number: "))

#addition = number1 + number2 + number3 
#average = addition / 3
#product = number1 * number2 * number3

#smallest = number1
#if number2 < smallest:
    #smallest = number2
#if number3 < smallest:
    #smallest = number3

#largest = number1
#if number2 > largest:
    #largest = number2
#if number3 > largest:
    #largest = number3

#print("Sum is", addition)
#print("Average is", average)
#print("Product is", product)
#print("Smallest is", smallest)
#print("Largest is", largest)