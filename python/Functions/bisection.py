def bisect(f,a,b,tol = 4*(2.**-52)):#Use bisection search in order to find the root of a function.
	''' bisect(func, left_endpt, right_endpt, tol)'''
	c = (a+b)/2.
    #Root-finding calculation
	from numpy import sign
	try:
		assert sign(f(a))!=sign(f(b))
		while abs((b-a)/2.)>=tol:
			c = (a+b)/2.
			if sign(f(c))!=sign(f(b)):
				a = c
			else:
				b = c
		return c

	except AssertionError:
		print '''Use Intermediate Value Theorem for bracket'''

