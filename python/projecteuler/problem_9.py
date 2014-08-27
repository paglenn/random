'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

# 0 < a < 500
# 0 < b < 500
def find_triple():
    for a in range(1,500):
        for b in range(a,500):
            c = 1000 - a - b
            if a**2 + b**2 == c**2 :
                triple = (a,b,c)
                return triple
from numpy import prod
print prod(find_triple())


