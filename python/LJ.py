from pylab import *
from numpy import *
m = 1
r = linspace(0.5,2,100)
LJ = -4*((1/r)**6 - (1/r)**12)
Go = 13/r**12 - 18/r**10 + 4/r**6
wGo = m*Go.copy()
SMOG = -6*(1./r)**6 + 5*(1./r)**12
plot(r,LJ,'r',label='6-12 LJ potential')
plot(r,SMOG,'b',label='10-12 potential (SMOG)')
xlabel(r'$r/\sigma$',fontsize=24)
ylabel(r'$u$',fontsize=24)
xlim(0.8,2.0)
ylim(-3,2)
legend(framealpha=0.5)
show()
#savefig('/Users/paulglen/Dropbox/Sp_2014/PHY 497 Honors Thesis in Physics/LJ.png')
