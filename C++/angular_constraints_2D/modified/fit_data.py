import numpy as np
from Pade_fit import Pade_fit

a = np.genfromtxt('hist.dat')
coeffs, ae, be = Pade_fit(a, 1, 0)
print coeffs
