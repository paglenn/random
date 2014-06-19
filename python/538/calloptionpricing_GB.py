# european-style call option pricing Monte-Carlo simulation
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st
from scipy.stats import *
S=20.; K=18.; r=0.05; T=1.; sigma=0.25
# S stock price,  K Strike Price,  r risk free rate, 
# T time to expiration in years, sigma volatility 
def blackscholes(S,K,r,T,sigma):  
    d1=(log(S/K)+(r+sigma**2/2)*T)/(sigma*sqrt(T))  
    d2=d1-sigma*sqrt(T)  # norm.cdf(x) = integral s from -infinity to x of 
#                                        (1/sqrt(2 Pi)) exp(-s^2/2) ds
#                          is cumulative distribution function
#                          for the normal distrubution
    BS= S*st.norm.cdf(d1)-K*exp(-r*T)*st.norm.cdf(d2)  
    return BS
bsvalue = blackscholes(S,K,r,T,sigma)
print 'Using Black-Scholes formula, Call option price =',bsvalue
M=25  # number of different trials
samplesizes = array([100,1000,10000])
colors = ['r','b','g'] # colors red, blue, green for plotting samplesize results
for iss in range(3):
   N = samplesizes[iss]
   color=colors[iss]
   Price=empty(M)
   for j in range(M):                                            # conduct M different trials
       finalstockprice=empty(N); calloptionvalue=empty(N) 
       z=np.random.randn(N)                                      # normally distributed random numbers
       for i in range(N):
           finalstockprice[i] = S*exp((r-0.5*sigma**2)*T+sigma*sqrt(T)*z[i]) # stock price at expiration t=T
           calloptionvalue[i] = max(finalstockprice[i]-K,0)                  # value of call option at t=T
       Price[j] = exp(-r*T)*calloptionvalue.mean()               # average over N samples, and compensate by factor
                                                                 # exp(-r*T) to give price at present t=0
   print 'Based on ',M,' samples, each of samplesize ',N
   print 'mean price=',Price.mean(),' variance=',Price.var()
   print 'error =',abs(Price.mean()-bsvalue)
   plt.plot(range(M),Price,color+'o')
   plt.plot([0.,25.],[Price.mean(),Price.mean()],color+'-')      # line showing mean for this samplesize
   plt.plot([0.,25.],[bsvalue,bsvalue],'k-',lw=1.0)              # black line showing Black-Scholes value
title='Samplesizes: N=100 red, N=1000 green, N=10000 blue'
plt.title(title)
plt.xlabel('trial number j')
plt.ylabel('Estimate of call option price')
plt.show()
