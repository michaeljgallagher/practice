'''
Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

All given inputs are in lowercase letters a-z.
'''

def longestCommonPrefix(strs):
    if strs == []:
        return ''
    strs.sort(key=len)
    res = ''
    for i in range(len(strs[0])):
        start = strs[0][i]
        for s in strs[1:]:
            if s[i] != start:
                return res
        res += start
        start = strs[0][i]
    return res

print(longestCommonPrefix(["flower","flow","flight"]) == 'fl')
print(longestCommonPrefix(["dog","racecar","car"]) == '')
