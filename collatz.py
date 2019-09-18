'''
A Collatz sequence in mathematics can be defined as follows.
Starting with any positive integer:

    if n is even, the next number in the sequence is n / 2
    if n is odd, the next number in the sequence is 3n + 1

It is conjectured that every such sequence eventually reaches the number 1.
Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?
'''

def collatz(n):
    seq = [n]
    while n > 1:
        if n % 2 == 0:
            n = int(n/2)
            seq.append(n)
        else:
            n = 3*n + 1
            seq.append(n)
    return seq

longest_length=0
longest_n = 0
for i in range(1,1000001):
    if longest_length < len(collatz(i)):
        longest_length = len(collatz(i))
        longest_n = i

print('The longest sequence length is {} with an n-value of {}'
      .format(longest_length, longest_n))
#print('Sequence:')
#print(collatz(longest_n))
