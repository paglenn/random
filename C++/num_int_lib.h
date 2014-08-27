double trapezoidal_rule(double a, double b, int n, double (*func)(double)) 
{
	double trapez_sum;
	double fa, fb, x, step;
	int j;
	step = (b-a)/((double) n);
	fa = (*func)(a)/2. ;
	fb = (*func)(b)/2. ;
	trapez_sum = 0.;
	for(j = 1; j< n; j++) {
		x = j*step + a;
		trapez_sum += (*func)(x);
	}
	trapez_sum = (trapez_sum+fb+fa)*step;  
	return trapez_sum; 
} // end trapezoidal_rule 

double simpson(double a, double b, int n, double (*func)(double)) 
{
	double sum= 0. ;
	double fa, fb, x, step; 
	
	step = (b-a)/((double) n) ;
	fa = (*func)(a)/2. ;
	fb = (*func)(b)/2. ;
	for(int j = 1; j<n; j++) {
		x = a + j*step; 
		
		int m;
		if( j%2 == 0) { m = 2;}
		else { m = 4; }
		
		sum += m * (*func)(x); 
	}
	sum = (sum + fa + fb)*step/3.;
} // end simpson's rule 

double gauleg



		

