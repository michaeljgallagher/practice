"""
You will be given two arrays of integers and asked to determine all integers 
that satisfy the following two conditions:

1. The elements of the first array are all factors of the integer being 
   considered
2. The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. You must 
determine how many such numbers exist.
"""

def getTotalX(a, b):
    b_common_factors = []
    for i in range(1,min(b)+1):
        if sum([x%i for x in b]) == 0:
            b_common_factors.append(i)
    between = []
    for i in b_common_factors:
        if sum([i%x for x in a]) == 0:
            between.append(i)
    return len(between)

a, b = [2, 4], [16, 32, 96]
print(getTotalX(a, b)==3)
a, b = [3, 4], [24, 48]
print(getTotalX(a, b)==2)
a, b = [1], [72, 48]
print(getTotalX(a, b)==8)
a, b = [1], [100]
print(getTotalX(a, b)==9)