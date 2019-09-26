def intToRoman(num):
    '''
    Given an integer, convert it to Roman numeral
    input num: int
    return s: string
    ''' 
    vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    s = ''
    for i, v in enumerate(vals):
        s += (num//v) * numerals[i]
        num %= v
    return s

print(intToRoman(14)) # 'XIV'
print(intToRoman(246)) # 'CCXLVI'
print(intToRoman(789)) # 'DCCLXXXIX'
print(intToRoman(2421)) # 'MMCDXXI'
