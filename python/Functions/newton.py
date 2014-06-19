def newton(f, fprime, x, tol):
	''' newton(f, fprime, x0, tol) '''
	counter=0
	while abs(f(x))>tol:
		step = -f(x)/fprime(x)
		x += step
		counter += 1
		if counter >=500: return
   	return x

