'''
Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of
zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

def three_sum(nums):
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            if nums[i] > 0:
                break
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                            l += 1
                    while l < r and nums[r] == nums[r-1]:
                            r -= 1
                    l += 1
                    r -= 1
        return res

a = [-1, 0, 1, 2, -1, -4]
b = [1,2,-2,-1]
c = [-1, 0, 1, 0]
print(three_sum(a) == [[-1, -1, 2], [-1, 0, 1]])
print(three_sum(b) == [])
print(three_sum(c) == [[-1, 0, 1]])





'''
def three_sum(nums):
        nums.sort()
        res = []
        for i, x in enumerate(nums[:-2]):
            temp = [x]
            for j, y in enumerate(nums[i+1:-1]):
                temp.append(y)
                if 0-(x+y) in nums[i+j+2:]:
                    temp.append(0-(x+y))
                    if sorted(temp) not in res:
                        res.append(temp)
                temp = [x]
        return res
'''
