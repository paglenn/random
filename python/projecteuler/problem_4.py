'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def last(n) : return n%10
def first(n) :
    k = m = 1
    while n/10.**(m+1) >= 1:
        m += 1
    while n/((k+1)*10**m) >= 1:
        k += 1
    return k

def pall(n):
    if first(n) != last(n): return False
    num = str(n)
    l = len(num)
    for j in range(l/2):
        if num[j] != num[l-j-1]:
            return False

    return True

a = 999
b = 999

for k1 in range(899):
    a -= k1
    if a%10 == 0: continue
    n = a*b
    for k in range(899):
        if (b-k)%10 == 0: continue
        n = a*(b-k)
        if pall(n): break

    if pall(n): break
print n
print pall(n)


