from scipy.optimize import newton

def g(z,w,h,f,t):
	return w + h * f(t,z) - z

def f(y,t):
	return t + y

def BackEuler(f,a,b,ya,n):
	h=(b-a)/float(n)
	w = ya
	for i in range(n+1):
		t = a + i*h
		w = newton(g,w, args=(w,h,f,t))
	return w

def euler(f,a,b,ya,n):
	h=(b-a)/float(n)
	w = ya
	for i in range(n+1):
		t = a + i*h
		w += h * f(w,t)
	return w
	
def embedRK23(f,a,b,ya,n):
	h=(b-a)/float(n)
	w = ya
	for i in range(n+1):
		t  = a + i*h
		s1 = f(t,w)
		s2 = f(t + h, w + h*s1)
		s3 = f(t + h/2., w + (h/4.)*(s1+s2))
		w = w + (h/2.)*(s1+s2)
		print w
		e = abs(h*(s1 - 2*s3 + s2)/3.)
		tol = .002
		if e <= .8*tol:
			h *= 2.
		else:
			h *= .5
	return w

ya = 0.
a = 0.
b = 1.
n = 10
print "Solution-ish:",0.71841775501

#yb = embedRK23(f,a,b,ya,n)


print BackEuler(f,a,b,ya,n)
print embedRK23(f,a,b,ya,n)
