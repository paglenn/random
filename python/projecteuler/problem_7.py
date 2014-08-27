'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

primes = [2,3]

n = 5
while len(primes) < 10001:
    flag = 0
    for p in primes:
        if n%p == 0 :
            n += 2
            flag = 1
            break
    if flag == 1: continue
    primes.append(n)

print primes[-1]
