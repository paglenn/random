'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# Algorithm: test an incremented num (by 20) for divisibility by 20,19,18,...

num = 20
divisors =range(1,num+1)
remove = [2,10,5,9,3,4,6,7,8,12,15]
for r in remove: divisors.remove(r)
x = num
while not all([x%y == 0 for y in divisors]):
    x += num
    print x

print x
