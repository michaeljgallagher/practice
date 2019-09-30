'''
Given a list of numbers, create an algorithm that arranges them in order to
form the largest possible integer.
For example, given [10, 7, 76, 415], you should return 77641510.
'''

def largestPossibleInteger(arr):
    res = ''
    values = []
    longest = len(str(max(arr))) + 1 #adding one simplifies this
    #lengthen and trim, append to list
    for x in arr:
        long_value = str(x) * longest
        #append as tuple to be able to recall original value
        values.append((long_value[:longest], str(x)))
    values.sort(reverse = True)
    for val in values:
        res += val[1]
    return int(res)

print(largestPossibleInteger([10, 7, 76, 415]) == 77641510)
print(largestPossibleInteger([90000, 99, 9, 123456]) == 99990000123456)
print(largestPossibleInteger([0, 90, 7]) == 9070)
print(largestPossibleInteger([0, 70, 9]) == 9700)
