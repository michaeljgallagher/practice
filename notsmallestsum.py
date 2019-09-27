'''
Given a sorted array, find the smallest positive integer that is not the sum of
a subset of the array.
For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.
'''

def solution(arr):
    res = 1
    for i in range(len(arr)):
        if res >= arr[i]:
            res += arr[i]
        else:
            break
    return res

print('returned: ' + str(solution([1, 2, 3, 10])) + ' expected: 7')
print('returned: ' + str(solution([1, 3, 4, 10])) + ' expected: 2')
print('returned: ' + str(solution([1, 1, 1, 1])) + ' expected: 5')
print('returned: ' + str(solution([4, 8, 12])) + ' expected: 1')
print('returned: ' + str(solution([1, 1, 3, 4])) + ' expected: 10')
print('returned: ' + str(solution([1, 1, 2, 3, 5, 8])) + ' expected: 21')
