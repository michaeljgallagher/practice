'''
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Note: Your solution should be in logarithmic time complexity.
'''

def trailingZeroes(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count

print(trailingZeroes(3) == 0)
print(trailingZeroes(5) == 1)
print(trailingZeroes(6) == 1)
print(trailingZeroes(7) == 1)
print(trailingZeroes(10) == 2)
print(trailingZeroes(0) == 0)
