#Program 6.4 Plotting program for one-body problem 
# Inputs: int=[a b] time interval, initial conditions
# ic = [x0 vx0 y0 vy0], x position, x velocity, y pos, y vel,
# h = stepsize, p = steps per point plotted
# Calls a one-step method such as trapstep.m
# Example usage: orbit([0., 100.],[0., 1., 2., 0.],0.01,5)
from numpy import *
def orbit(int=None, ic=None, h=None, p=None):
    n = around((int[1] - int[0])/(p * h))# plot n points
    t = empty([p+1]); tp = empty([n+1])
    x0, vx0, y0, vy0 = ic   # grab initial conds
    m = shape(ic)[0]
    y = empty([p+1,m]); yp = empty([n+1,m])
    y[0,:] = hstack([x0, vx0, y0, vy0]); yp[0,:] = y[0,:]
    t[0] = int[0]; tp[0] = t[0] # build y vector
#    set(gca, mstring('XLim'), mcat([-5, 5]), mstring('YLim'), mcat([-5, 5]), mstring('XTick'), mcat([-5, 0, 5]), mstring('YTick'), mcat([-5, 0, 5]), mstring('Drawmode'), mstring('fast'), mstring('Visible'), mstring('on'), mstring('NextPlot'), mstring('add'))
#    cla
#    sun = line(mstring('color'), mstring('y'), mstring('Marker'), mstring('.'), mstring('markersize'), 25, mstring('xdata'), 0, mstring('ydata'), 0)
#    drawnow
#    head = line(mstring('color'), mstring('r'), mstring('Marker'), mstring('.'), mstring('markersize'), 25, mstring('erase'), mstring('xor'), mstring('xdata'), mcat([]), mstring('ydata'), mcat([]))
#    tail = line(mstring('color'), mstring('b'), mstring('LineStyle'), mstring('-'), mstring('erase'), mstring('none'), mstring('xdata'), mcat([]), mstring('ydata'), mcat([]))
    #[px,py,button]=ginput(1);         % include these three lines
    #[px1,py1,button]=ginput(1);       % to enable mouse support
    #y(1,:)=[px px1-px py py1-py];     % 2 clicks set direction
    
    for k in range(len(n)):    
        for i in range(len(p)):        
            t[i+1] = t[i] + h        
            y[i + 1,:] = eulerstep(t[i], y[i, :], h)        
        y[0,:] = y[p,:]; yp[k+1,:] = y[p,:]        
        t[0] = t[p];    tp[k+1] = t[p]
#        set(head, mstring('xdata'), y(1, 1), mstring('ydata'), y(1, 3))    
#        set(tail, mstring('xdata'), y(mslice[2:p], 1), mstring('ydata'), y(mslice[2:p], 3))    
#        drawnow    
    return [tp,yp]

def eulerstep(t=None, x=None, h=None):
    #one step of the Euler method
    return x + h * ydot(t, x)

def ydot(t=None, x=None):
    m2 = 3    
    g = 1;    
    mg2 = m2 * g;    
    px2 = 0;    
    py2 = 0;
    px1, py1, vx1, vy1 = x
    dist = sqrt((px2-px1)**2 + (py2-py1)**2)
    return array([vx1,(mg2 *(px2-px1))/(dist**3),vy1,(mg2*(py2-py1))/(dist**3)])
 
tp,yp=orbit([0., 100.],[0., 1., 2., 0.],0.01,5)
print 'tp='
print tp
print 'yp='
print yp
   
import time
import numpy as np
import matplotlib
matplotlib.use('TkAgg') # do this before importing pylab
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

def animate():
    tp,yp=orbit([0., 10.],[0., 1., 2., 0.],0.01,5)
    tstart = time.time()                   # for profiling
    ntp = shape(tp)[0]
    print 'ntp=',ntp
    xx=hstack([yp[0,0],yp[ntp-1,0]])
    yy=hstack([yp[0,2],yp[ntp-1,2]])
    line ,= ax.plot(xx,yy)

    for i in range(ntp-2):
        line.set_xdata(yp[i:2+i,0])          # update the data
        line.set_ydata(yp[i:2+i,2])
        fig.canvas.draw()                         # redraw the canvas
    print 'FPS:' , 200/(time.time()-tstart)

win = fig.canvas.manager.window
fig.canvas.manager.window.after(100, animate)
plt.show()
