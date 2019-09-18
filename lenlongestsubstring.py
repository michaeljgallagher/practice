def lenLongestSubStr(s):
    '''
    Given a string, find the length of the longest substring
    without repeating characters.
    '''
    used = {}
    max_length = start = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_length = max(max_length, i - start + 1)
        used[c] = i
    return max_length

print(lenLongestSubStr('abcabcbb')) # 'abc', length of 3
print(lenLongestSubStr('bbbbb')) # 'b', length of 1
print(lenLongestSubStr('pwwkew')) # 'wke', length of 3
