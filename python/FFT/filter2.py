import numpy as np
import math as m

def filter(signal,timestep=1.0,higherCutoff=np.inf, lowerCutoff=0):
	signal_fft = np.fft.fft(signal)
	frequencies = np.fft.fftfreq(signal.size,d=timestep)
	for freq in frequencies:
		if abs(freq) > higherCutoff or abs(freq) < lowerCutoff:
			signal_fft[np.where(frequencies == freq)[0]] = 0
	return np.fft.ifft(signal_fft)

dt = 0.01
N = int(2/dt)
t = np.linspace(-1,1,N)
y  = np.zeros(N) ; y[N/4+1:3*N/4+1] = 1.

yf = np.real( filter(y, dt,higherCutoff=15*m.pi) )

import matplotlib.pyplot as plt
plt.plot(t,y,label='original')
plt.plot(t,yf,label='filtered')
plt.xlim(-1.1,1.1)
plt.ylim(-0.1,1.1)
plt.legend()
plt.show()







