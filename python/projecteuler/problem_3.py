'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

# 1st attempt: compute all primes up to sqrt(num) with the sieve of eratosthenes .

import math
N = 600851475143
sqrtN = int( math.sqrt(N) ) + 1
sieve = range(sqrtN)

for n in range(2,sqrtN) :

    if sieve[n] == 0: continue
    if n != 2 and n%2 == 0:
        sieve[n] = 0
        continue

    x = 2*n
    while x < sqrtN :
        sieve[x] = 0
        x += n
p = 0
for x in sieve:
    if x != 0 and N%x == 0:
        # then x is a prime factor
        p = x
        # this works because the order is increasing x
print p
# check!








