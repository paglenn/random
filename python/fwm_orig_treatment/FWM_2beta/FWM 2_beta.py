#Calculates four-wave-mixing effects at the 2*beta frequency. 
import math as mth
eta0=1.0; etab=1.0; etanb=1.0
alphab=0.0; alphanb=0.0; alpha0=0.0
tslot=20.0; nbmax=1001;
nmaxt=nbmax-1; tmax=+5.000; tmin=-5.000
nmaxz=10**4; zmin=-10.0; zf=5.0
beta=10
yb=-1.0*tslot; ynb=+1.0*tslot; y0=0.0
phi=[0 for k in range(nbmax)]
delta=10**(-10);

dz=(zf-zmin)/nmaxz
dt=(tmax-tmin)/nmaxt

zc=-yb/(2*beta)
print zc
f = open('fwm5.txt','w')

#Begin loop over t
t=tmin
for k in range(nbmax):
    z=zmin+0.5*dz
    s1=0.0
    s2=0.0
    s3=0.0
    s4=0.0
    x0=eta0*t
    for j in range(nmaxz):
        xb=etab*(t-yb-2*beta*z)
        xnb=etanb*(t-ynb+2*beta*z)
        chi0=alpha0+(eta0**2)*z
        chib=alphab+beta*(t-yb)+z*((etab**2)-beta**2)
        chinb=alphanb-beta*(t-ynb)+z*((etanb**2)-beta**2)
        s1+=mth.sin(2*chib-chi0)/((mth.cosh(xb)**2))
        s2+=mth.cos(2*chib-chi0)/((mth.cosh(xb)**2))
        s3+=mth.sin(chib-chinb+chi0)/(mth.cosh(xb)*mth.cosh(xnb))
        s4+=mth.cos(chib-chinb+chi0)/(mth.cosh(xb)*mth.cosh(xnb))
        z+=dz
    phi[k]=(2.0*(etab**2)*eta0*dz*mth.sqrt((s1)**2+(s2)**2) + 4.0*eta0*etab*etanb*dz*mth.sqrt((s3)**2+(s4)**2))/mth.cosh(x0)
    if abs(t)<delta:
        f.write(str(0.0)+" "+str(phi[k])+'\n')
    else:
        f.write(str(t)+" "+str(phi[k])+'\n')
    t+=dt

f.close()
print "done!"
