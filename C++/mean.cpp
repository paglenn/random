// calculate mean and standard deviation of a created data set 
// from Computational Physics by Hjorth - Jensen
#include<iostream>
#include<cmath>
using namespace std; 

int main() {
	int i;
	float sum, sumsq2, xbar, sigma1, sigma2;
	float x[127];

	// initialize the data set 
	for(i=0; i < 127; i++) { x[i] = i+ 100000.; }

	sum = 0.; // sum over all elements 
	sumsq2 = 0.; //sum over all squares 

	//Text book algorithm 
	for(i = 0; i<127; i++ ) {
		sum += x[i];
		sumsq2 += pow(x[i],2) ;
	}
	//calculate mean and stdev
	xbar = sum/127;
	sigma1 = sqrt((sumsq2-sum*xbar)/126.);

	/*
	 * Here comes the cruder algorithm where we evaluate 
	 * separately first the average and thereafter the sum 
	 * which defines the standard deviation. The average 
	 * has already been evaluated through xbar
	 */

	sumsq2 = 0;
	for(i = 0; i<127; i++) {
		sumsq2 += pow((x[i]-xbar),2.);
	}
	sigma2 = sqrt(sumsq2/126.) ;
	
	cout << "xbar = "<< xbar << " sigma1 = "<< sigma1 << " sigma2 = "<< sigma2; 
	cout<<endl;

	return 0;
} //end main
