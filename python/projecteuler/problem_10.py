'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
# Use the sieve of eratosthenes

N = int(2e6 )
sieve = range(N)
s = 0
num_primes = 0

for n in range(2,N) :

    if sieve[n] == 0: continue
    if n != 2 and n%2 == 0:
        sieve[n] = 0
        continue

    s += n
    num_primes += 1
    x = 2*n
    while x < N :
        sieve[x] = 0
        x += n

print s
print num_primes
