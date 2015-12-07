#include<iostream>
#include<cmath>
#include "MersenneTwister.h"
#include<fstream>
#include<iomanip>
using namespace std ; 
int main() { 
	
	int L = 1 ; 
	double C = 0.05 ; 
	double tol = 0.005 ; 
	double dx = 0.05 ; 
	double x1, x2  ;
	x1 = x2 = sqrt(C) ; 
	double x[2] = {x1,x2} ; 
	int nsteps = 2e8 ; 
	int i ; //iteration 
	int acc; 
	double pct_acc ;
	MTRand gen; 
	gen.seed() ; 
	ofstream fout ;
	fout.open("p1_hist.dat") ;
	int sf = 200 ; 
	int eqTime = 200  ; 
	const int nbins = 100 ; 
	int hist[nbins] ; 
	int TC = 0 ; 
	int ip, jp;


	for( int i = 0 ; i < nsteps ; i++) { 

		ip = gen.randInt()%2 ; 
		jp = 1-ip ; 
		double delx = (2 * gen.rand() - 1) * dx  ; 
		double xip = x[ip] + delx ;
		double xjp = C / xip; 

		acc = 0 ; 
		if (xip < 0 || xip > 1 || xjp> 1 || xjp < 0) acc = 0; 
		else {
			if ( gen.rand() < x[ip]/ xip ) acc = 1 ;
		}

		if (acc) {
			x[ip] = xip ; 
			x[jp] = xjp ; 
			pct_acc +=  1; 
		}

		if(i%sf == 0 && i > eqTime  ) { 
			int bin_index = floor(x[ip] * nbins ) ; 
			hist[bin_index] += 1 ; 
			TC += 1  ;

		}

	}

	double P ; 
	double binCenter; 
	double xbar = 0; 
	for(int b = 0 ; b < nbins ; b++ ) { 
		binCenter = (b+0.5)  / nbins; 

		P = hist[b] / (double) TC; 
		xbar += binCenter * P ; 
		if( hist[b] > 0) fout << log(binCenter) << setw(15) <<  log(P) << endl ;	
	}
	cout << xbar << endl ;
	cout << "acc rate: "<< pct_acc / (double) nsteps << endl ;
	


	
}
