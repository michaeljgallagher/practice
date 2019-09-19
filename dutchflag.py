'''
Given an array of strictly the characters R, G, and B, segregate the values
of the array so that all of the Rs come first, the Gs come second, and the
Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], you should
transform it to ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
'''

def transform(arr):
    low, mid, high = 0, 0, len(arr)-1 #indices dividing array
    while mid <= high:
        if arr[mid] == 'R':
            #swap to left-most section, increment low & mid indices
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        elif arr[mid] == 'G':
            #do nothing (already in mid section), increase middle index
            mid += 1
        else: #arr[mid] == 'B'
            #swap to right-most section, decrement high index
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

###################
import random
arr = [random.choice(['R', 'G', 'B']) for _ in range(20)]
print('Array to sort:\n{}'.format(arr))
print('Sorted array:\n{}'.format(transform(arr)))
