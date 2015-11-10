import numpy as np

# binary search
I = [0,0.5]
seq = (0,1,0,0,1,1,0,0,0,1,0,1,1,0,1,1,1,0,1,1)


for n in range(1,20) :
    if seq[n-1] == 0 :
        if seq[n] == 0 :
            I[1] -= (0.5)**(n+1)
        elif seq[n] == 1 :
            I[0] += (0.5)**(n+1)
    else:
        if seq[n] == 1 :
            I[1] -= (0.5)**(n+1)
        elif seq[n] == 0 :
            I[0] += (0.5)**(n+1)

print I

# 2nd try
I = [0.5,1]
for n in range(20)[::-1]:
    bn = seq[n]
    I[0] = bn + (0.5-bn)*I[0]
    I[1] = bn + (0.5-bn)*I[1]

print I




print 'check:'
def f(x) :
    if x <= 0.5 :
        return 2*x
    elif x >= 0.5  and x <= 1.0:
        return 2*(1-x)
    else:
        print x , ' > 1'
        quit()

nsteps = 20
y = 0.5 * (I[0]+ I[1])
print y
print I[1] - I[0]

myseq = [round(y,0)]

for i in range(nsteps-1):
    if i%2 == 0 :
        y = f(y)*(1+np.pi*1e-16)
    else:
        y = f(y)*(1-np.pi*1e-16)

    myseq.append(round(y))

print myseq



