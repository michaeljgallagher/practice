'''
Given a non-empty array of digits representing a non-negative integer, plus one
to the integer.
The digits are stored such that the most significant digit is at the head of
the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number
0 itself.
'''

def plus_one(digits):
    i = len(digits) - 1
    while digits[i] == 9 and i > 0:
        digits[i] = 0
        i -= 1
    if i == 0 and digits[0] == 9:
        digits = [1, 0] + digits[1:]
    else:
        digits[i] += 1
    return digits

print(plus_one([1,2,3]) == [1,2,4])
print(plus_one([4,3,2,1]) == [4,3,2,2])
print(plus_one([0]) == [1])
print(plus_one([9]) == [1,0])
print(plus_one([9,9,9,9]) == [1,0,0,0,0])
print(plus_one([1,4,9,9]) == [1,5,0,0])
