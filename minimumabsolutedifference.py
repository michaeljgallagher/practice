'''
Given an array of distinct integers arr, find all pairs of elements with the
minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair
[a, b] follows

    a, b are from arr
    a < b
    b - a equals to the minimum absolute difference of any two elements in arr
    
'''

def minAbsDiff(arr):
    arr.sort()
    diff = float('Inf')
    res = []
    for i in range(1, len(arr)):
        cur_diff = arr[i] - arr[i-1]
        if cur_diff < diff:
            diff = cur_diff
            res = [[arr[i-1], arr[i]]]
        elif cur_diff == diff:
            res.append([arr[i-1], arr[i]])
        else:
            continue
    return res

print('Input: arr = [4,2,1,3]\nExpecting: [[1, 2], [2, 3], [3, 4]]')
print('Result: {}'.format(minAbsDiff([4,2,1,3])))

print('Input: arr = [1,3,6,10,15]\nExpecting: [[1, 3]]')
print('Result: {}'.format(minAbsDiff([1,3,6,10,15])))

print('Input: arr = [3,8,-10,23,19,-4,-14,27]\
        \nExpecting: [[-14, -10], [19, 23], [23, 27]')
print('Result: {}'.format(minAbsDiff([3,8,-10,23,19,-4,-14,27])))

