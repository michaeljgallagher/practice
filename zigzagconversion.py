'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this: (you may want to display this pattern in a fixed font for
better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number
of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows < 2: #Base case; doesn't zigzag
        return s
    rows = [""] * numRows #string for each row
    i = -1 #index, start at -1 because first step will add to 0 as desired
    direction = 1 #1 = down, -1 = up
    for c in s:
        i += direction
        rows[i] += c       
        if i == 0:
            direction = 1
        elif i == numRows - 1:
            direction = -1
    return "".join(rows)

print(convert('PAYPALISHIRING', 3)) #'PAHNAPLSIIGYIR'
print(convert('PAYPALISHIRING', 4)) #'PINALSIGYAHRPI'
