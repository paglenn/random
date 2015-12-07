from Pade_fit import Pade_fit, Pade_eval
import numpy as np

a = np.genfromtxt('p1_hist.dat' )
coeffs, ae, be = Pade_fit(a, 1, 0)
print coeffs, ae, be
