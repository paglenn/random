'''

[file problem_8.txt]

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
'''
from numpy import prod

data = open('problem_8.txt','r')
number = data.readline()
number = number[:-1]

s = 0
S = []
for i in range(1000-13):
    section = list(number[i:i+13])
    section = [int(x) for x in section]
    if prod(section) > s: s = prod(section)
    S.append(prod(section))

print s
print max(S)

