'''
Implement the function fib(n), which returns the nth number in the Fibonacci
sequence, using only O(1) space.
'''

def fib(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(2, n+1):
            c = b + a
            a = b
            b = c
        return c
