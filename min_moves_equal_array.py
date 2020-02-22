'''
Given a non-empty integer array of size n, find the minimum number of moves
required to make all array elements equal, where a move is incrementing
n - 1 elements by 1.
'''


def min_moves(nums):
    mini = min(nums)
    count = 0
    for x in nums:
        count += x - mini
    return count


print(min_moves([1,2,3]) == 3)
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
