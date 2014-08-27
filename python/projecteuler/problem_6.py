'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

# This is actually commonn practice for me: the difference is simply
# 2 times the cross terms between the first N numbers.

N = 100
s = 0
for i in range(1,N+1):
    for j in range(i+1,N+1):
        s += 2*i*j
print s



