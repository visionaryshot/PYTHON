def maximum(max, min):
    return max if max > min else min

highest_number = reduce(maximum, [3, 5, 9, 2, 8])
print(highest_number)  
