#include<cmath> 

#ifndef MATHEMATX_H_
#define MATHEMATX_H_ 

const long double PI = acos(-1.0) ; 

double atan_proper(double x, double y) { 
	double theta ; 
	if (x == 0 ) {
		if (y > 0) theta =  PI/2.0 ; 
		else if (y < 0) theta =  PI/2.0 ; 
	} else {
		theta = atan(y/x ) ; 
		if(x > 0 and y > 0 ) {
			theta = theta ; 
		} else if (x > 0 && y< 0) {
			theta = theta + 2*PI ; 
		} else {
			theta = theta + PI ; 
		}
	}
	return theta ; // never runs 
}

bool diff(double a, double b, double eps = 1e-16 ) { 
	return fabs(a-b) > eps ; 
}

int sgn(double val) { 
	return (val > 0 ) - (val < 0) ; 
}

#endif 
