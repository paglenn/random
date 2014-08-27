import numpy as np
import math as m

def lockIn(signal,ref):
	sFFT = np.fft.fft(signal)
	rFFT = np.fft.fft(ref)
	product = sFFT * rFFT
	return np.fft.ifft(product)

t = np.linspace(-10,10,100)
y = np.sin(t)
yn = 5*np.sin(50*t) + np.fft.ifft(np.fft.fft(y) + 5*np.random.rand(100) )
yf = np.real( lockIn(yn,y) )

import matplotlib.pyplot as plt
plt.plot(t,yn,label='noisy signal')
plt.plot(t,yf,label='filtered signal')
plt.plot(t,y,label='original signal')
plt.legend()
plt.show()



