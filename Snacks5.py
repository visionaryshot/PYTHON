a = 62
b = 98
c = 85

if a > b and a > c:
    largest = a
    if b > c:
        second_largest = b
    else:
        second_largest = c
elif b > a and b > c:
    largest = b
    if a > c:
        second_largest = a
    else:
        second_largest = c
else:
    largest = c
    if a > b:
        second_largest = a
    else:
        second_largest = b

print("Largest:", largest)
print("Second largest:", second_largest)