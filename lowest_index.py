'''
Given a sorted array arr of distinct integers, return the lowest index i for
which arr[i] == i. Return null if there is no such index.

For example, given the array [-5, -3, 2, 3], return 2 since arr[2] == 2.
Even though arr[3] == 3, we return 2 since it's the lowest index.
'''


def lowest_index(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return None


print(lowest_index([-5, -3, 2, 3]) == 2)


# Alternatively, we see that the lowest index could be -3 if we choose to
# include negative indices

def lowest_index_2(arr):
    for i in range(len(arr)):
        if arr[i] == i or arr[i] == -len(arr)+i:
            return arr[i]
    return None


print(lowest_index_2([-5, -3, 2, 3]) == -3)
print(lowest_index_2([-5, -1, 2, 3]) == 2)
