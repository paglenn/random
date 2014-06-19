def rk4(x, y, f, h):
        ''' 4-th order Runge Kutta for ODE.'''
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5*h, y + 0.5*k1)
        k3 = h * f(x + 0.5*h, y + 0.5*k2)
        k4 = h * f(x + h, y + k3)
        return y + (k1 + 2*(k2 + k3) + k4)/6.0
