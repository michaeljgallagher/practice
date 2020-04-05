'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

def divisors(n):
    return [x for x in range(1, n) if n % x == 0]


def main():
    res = [0 for _ in range(10001)]
    amicable = []

    for i in range(10001):
        res[i] = sum(divisors(i))
        try:
            if res[res[i]] == i and i != res[i]:
                if i not in amicable:
                    amicable += [i, res[i]]
        except:
            continue
    print(sum(amicable))


if __name__ == '__main__':
    main()
