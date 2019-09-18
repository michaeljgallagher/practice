def romanToDecimal(s):
    '''
    Given a number in Roman numeral format, convert it to decimal
    input s: string
    return result: int
    '''   
    numeralDict = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
    }
    result = 0
    i = 0
    while i < len(s):
        num1 = numeralDict[s[i]]       
        if i+1 < len(s):
            num2 = numeralDict[s[i+1]]
            if num1 >= num2:
                result += num1
                i += 1
            else:
                result += num2 - num1
                i += 2
        else:
            result += num1
            i += 1
    return result

print(romanToDecimal('XIV')) #14
print(romanToDecimal('CCXLVI')) #246
print(romanToDecimal('DCCLXXXIX')) #789
print(romanToDecimal('MMCDXXI')) #2421
