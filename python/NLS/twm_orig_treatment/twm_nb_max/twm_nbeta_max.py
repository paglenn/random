import math as mth
eta0=1.0; etab=1.0; zc=1;
beta=10; tslot=20;
nbmax= 101; nmaxz= 10**4; zmin= -15.0;
nmaxt=nbmax-1;tmax=5.0;tmin=-5.0
a0= 0.0; ab= 0.0; 
y=0.0
yb=-tslot;
phi=[0 for x in range(nbmax)]

f = open('twmX.txt','w')
#Begin calculation with loop over zf
for i in range(51):
    zf=0.1*i
    dz=(zf-zmin)/nmaxz
    dt=(tmax-tmin)/nmaxt
#Loop over t
    t=tmin
    for k in range(nbmax):
        s1=0.0
        s2=0.0
        x0=eta0*t
        z=zmin+0.5*dz
        for j in range(nmaxz):
            xb=etab*(t-yb-2*beta*z)
            chi=2*(a0+(eta0**2)*z)-ab-beta*(t-yb)-(etab**2-beta**2)*z
            s1=s1+mth.sin(chi)/mth.cosh(xb)
            s2=s2+mth.cos(chi)/mth.cosh(xb)
            z=z+dz
        phi[k]=2.0*eta0*(etab**2)*mth.sqrt(s1**2+s2**2)*dz/mth.cosh(x0)**2
        t+=dt
#Capture maximum of phi
    P=max(phi);z=zf;
    f.write(str(z)+' '+str(P)+'\n')
    print zf,max(phi)
f.close()
print "done!"
