'''
Suppose you are giving a binary tree represented as an array.
For example, [3, 6, 2, 9, -1, 10] retpresents the following binary tree,
where -1 indicates it is a NULL node.

Write a function that determines whether the left or right branch of the tree
is larger. The size of each branch is the sum of the node vlaues. The function
should return the string “Right” if the right side is larger and “Left” if the
left side is larger. If the tree has zero nodes or if the size of the branches
are equal, an empty string “” should be returned.
'''

def traverse(arr, i):
    if i < len(arr):
        if arr[i] == -1:
            return 0
        return arr[i] + traverse(arr, (2*i)+1) + traverse(arr, (2*i)+2)
    return 0


def solution(arr):
    if not arr:
        return ''
    left = traverse(arr, 1)
    right = traverse(arr, 2)
    if left == right:
        return ''
    return 'Left' if left > right else 'Right'


print(solution([3, 6, 2, 9, -1, 10]) == 'Left')
