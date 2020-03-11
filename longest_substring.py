from collections import Counter

def longest_substring(s, k):
    count = Counter(s)
    st = max_st = 0
    for i, c in enumerate(s):
        if count[c] < k:
            max_st = max(max_st, longest_substring(s[st:i], k))
            st = i + 1
    return len(s) if st == 0 else max(max_st, longest_substring(s[st:], k))


print(longest_substring('aaabb', 3))
print(longest_substring('ababbc', 2))
