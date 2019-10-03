'''
Given an array nums of n integers and an integer target, find three integers in
nums such that the sum is closest to target. Return the sum of the three
integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''

def threesum(nums, target):
    nums.sort()
    closest = sum(nums[:3])
    for i in range(len(nums)-2):
        l = i+1
        r = len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == target:
                return target
            if abs(target-total) < abs(closest-target):
                closest = total
            if total < target:
                l+=1
            elif total > target:
                r-=1
    return closest

print(threesum([-1,2,1,-4], 1) == 2)
print(threesum([1,1,1,0], 100) == 3)
print(threesum([1,1,1,0], -100) == 2)
