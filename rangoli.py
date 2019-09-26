'''
You are given an integer, N. Your task is to print an alphabet rangoli of size
N. (Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''

from string import ascii_lowercase as letters

def print_rangoli(n):
    row = []
    for i in range(n):
        s = '-'.join(letters[i:n])
        row.append((s[::-1]+s[1:]).center(4*(n-1)+1, '-'))
    for x in reversed(row):
        print(x)
    for x in row[1:]:
        print(x)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
