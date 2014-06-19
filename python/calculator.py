from math import pi

h = 6.626e-34
k = 1.38e-23
hbar = h/(2*pi)
T = 300
c = 299792458
C = (32* (pi**5.) *(k**4.))/(15*(c*h)**3.) * (T**3.)
print C

R = 8.314
ratio = C/(3*R)
print ratio
