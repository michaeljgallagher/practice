'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Note: 1 is typically treated as an ugly number.
'''

def is_ugly(num):
    if num == 0:
        return False
    
    factors = [2, 3, 5]
    
    for p in factors:
        while num % p == 0:
            num /= p
    
    return num == 1


print(is_ugly(6) == True)
print(is_ugly(8) == True)
print(is_ugly(14) == False)
