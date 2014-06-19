#Examples of function definitions.
#Create one for integration?
def withinEpsilon(x, y, epsilon):
    """x,y,epsilon floats, epsilon>0.0
    returns True if x is within epsilon of y"""
    return abs(x - y) <= epsilon
##def f(x):
##    x=x+1
##    print 'x=', x
##    return x
##
##
##x=1
##z=f(x)
##print 'z=', z
##print 'x=', x

def isEven(i):
    """assume i a positive int
    returns True if i is even, otherwise False"""
    return i%2==0

#assert stops code dead in its tracks if False is returned
def findRoot(pwr,val,epsilon):
    """ assumes pwr an int; val, epsilon floats
    pwr and epsilon>0
    if it exists,
        returns a value withing epsilon of val**pwr
        otherwise returns None"""
    assert type(pwr)==int and type(val)==float\
           and type(epsilon)==float
    assert pwr>0 and epsilon>0
    if isEven(pwr) and val<0:
        return None
    low=-abs(val)
    high=max(abs(val),1.0)
    ans=(high+low)/2.0
    while not withinEpsilon(ans**pwr, val, epsilon):
        #print 'ans= ', ans, 'low= ', low, 'high= ', high
        if ans**pwr<val:
            low=ans
        else:
            high=ans
        ans=(high+low)/2.0
    return ans

sumDigits=0
for c in str(1952):
    sumDigits+=int(c)
print sumDigits
