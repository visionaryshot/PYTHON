count = 1
largest = 0
second_largest = 0

while count <= 10:
    number = int(input("Enter any number : "))

    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number

    count = count + 1

print("The largest number is", largest)
print("The second largest number is", second_largest)
