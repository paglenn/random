#find sq root by bisection
x=0.1
epsilon=0.01 # tolerance
numGuesses=0
low=0.0
high=x
ans=(high+low)/2.0
while abs(ans**3-x)>=epsilon and ans <=x:
   # print low, high, ans
    numGuesses+=1
    if ans**3 <x:
        low=ans
    else:
        high=ans
    ans=(high+low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is within', epsilon, 'of the cube root of', x
