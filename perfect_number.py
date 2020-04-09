'''
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
'''

def digit_check(n):
    return sum([int(d) for d in str(n)]) == 10

def perfect_n(n):
    num = 0
    x = 18
    while num < n:
        x += 1
        if digit_check(x):
            num += 1
    return x


print(perfect_n(1) == 19)
print(perfect_n(2) == 28)
print(perfect_n(100) == 1423)
