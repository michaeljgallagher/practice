'''
A fixed point in an array is an element whose value is equal to its index. 
Given a sorted array of distinct elements, return a fixed point, if one exists. 
Otherwise, return False.
For example, given [-6, 0, 2, 40], you should return 2. 
Given [1, 5, 7, 8], you should return False.
'''

def fixed_point(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return False

print(fixed_point([-6, 0, 2, 40]))
print(fixed_point([1, 5, 7, 8]))