'''
Given a non-empty array of integers, return the k most frequent elements.
'''

from collections import Counter

def top_k_frequent(nums, k):
    counter = Counter(nums)
    return sorted(counter, key=counter.get, reverse=True)[:k]


print(top_k_frequent([1,1,1,2,2,3], 2) == [1,2])
print(top_k_frequent([5, 5, 1, 4, 3, 4, 5, 2, 3, 2], 3) == [5,4,3])
