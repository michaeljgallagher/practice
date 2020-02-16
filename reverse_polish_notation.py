"""
Reverse Polish Notation calculator
"""


def rpn(s):
    stack = []
    for x in s.split():
        if x not in ['+', '-', '*', '/']:
            stack.append(x)
        else:
            a = stack.pop()
            b = stack.pop()
            res = str(eval(b + x + a))
            stack.append(res)
    return float(stack.pop())


print(rpn('15 7 1 1 + - / 3 * 2 1 1 + + -') == 5)
print(rpn('2 3 + 1 -') == 4)
print(rpn('4 2 5 * + 1 3 2 * + /') == 2)
