#Find the cube root of a perfect cube (Brute Force/Exhaustive Enumeration)

x=int(raw_input('Enter an integer: '))
ans=0
while ans*ans*ans<abs(x):
    ans=ans+1
if ans*ans*ans !=abs(x):
    print x, 'is not a perfect cube'
else:
    if x<0:
        ans=-ans
    print 'Cube root of'+str(x)+'is'+str(ans)
