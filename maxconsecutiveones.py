'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
'''

def findMaxConsecutiveOnes(nums):
    max_length = 0
    count = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            max_length = max(max_length, count)
            count = 0
    return max(max_length, count)

print(findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3)
