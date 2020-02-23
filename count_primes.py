'''
Count the number of prime numbers less than a non-negative number, n.
'''

def count_primes(n):
    if n <= 2:
        return 0
    
    is_prime = [True for _ in range(n)]
    is_prime[0] = False
    is_prime[1] = False
    
    for i in range(2, int(n**.5)+1):
        if is_prime[i]:
            for j in range(i**2, n, i):
                is_prime[j] = False
    primes = [p for p in range(2, n) if is_prime[p]]
    return len(primes)


print(count_primes(10) == 4)
print(count_primes(100) == 25)
print(count_primes(1000) == 168)
