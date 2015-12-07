#include<iostream>
#include<cmath>
#include "MersenneTwister.h"
#include<fstream>
#include<iomanip>
using namespace std ; 
int main() { 
	
	double r = 0.4  ; 
	double ss = 0.15 ; 
	double x1, x2  ;
	int nsteps = 1e8 ; 
	int i ; //iteration 
	int acc; 
	double pct_acc ;
	double pi = acos(-1 )  ;


	x1 = x2 = r/2.  ; 
	double th[2] = {acos(x1),acos(x2)} ; 
	double x[2] = {x1, x2 } ; 
	MTRand gen; 
	gen.seed() ; 
	ofstream fout ;
	fout.open("hist.dat") ;
	int sf = 2 ; 
	int eqTime = 10000  ; 
	const int nbins = 100 ; 
	int hist[nbins] ; 
	int TC = 0 ; 
	int ip, jp;


	for( int i = 0 ; i < nsteps ; i++) { 

		ip = gen.randInt()%2 ; 
		jp = 1-ip ; 
		double dth = (2 * gen.rand() - 1) * ss *pi ; 
		double thip = th[ip] + dth ; 
		double xip = cos(thip) ;
		thip = acos(xip) ; 
		double xjp =  r - xip  ; // what if r - xip > 1 (or < -1)? 
		double thjp = acos(xjp) ; 

		acc = 0 ; 
		if ( gen.rand() < fabs( sin(th[jp])/sin(thjp) ) && fabs(r-xip) <= 1 ) acc = 1 ;
		if (acc) {
			//cout << thip << endl;
			x[ip] = xip ; 
			x[jp] = xjp ; 
			th[ip] = thip  ; 
			th[jp] = thjp  ; 
			pct_acc +=  1; 
		}

		if(i%sf == 0 && i > eqTime  ) { 
			int bin_index = floor( th[ip] * nbins/ (pi) ) ; 
			//cout << bin_index  << " " << nbins << endl ;
			hist[bin_index] += 1 ; 
			
			TC += 1  ;
		}

	}

	double P ; 
	double binCenter; 
	double xbar = 0; 
	for(int b = 1 ; b +1< nbins ; b++ ) { 
		binCenter = pi*(b+0.5)  / nbins; 

		P = hist[b] / (double) TC; 
		xbar += cos(binCenter) * P ; 
		if( hist[b] > 100) {
			fout << log(1 - pow(r -cos(binCenter),2)) ; 
			fout <<  setw(16) << log(P) ;	
			fout << endl ;
		}
	}
	cout << xbar << endl ;
	cout << "acc rate: "<< pct_acc / (double) nsteps << endl ;
	


	
}
