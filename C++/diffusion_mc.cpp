// diffusion_mc.cpp 
// By: Paul Glenn 
// diffusion in 1 dimension 
#include<iostream>
#include<ctime>
#include<cstdlib>
#include<fstream>
#include<iomanip>
#include<string>
#include<cmath>
using namespace std;

double std_dev(double data[], int size, double avg);

ofstream outfile; 
int main(int argc, char* argv[]) {
	
	if(argc < 3) { 
		cout<< "Usage: ./a.out [num_particles] [num_steps] ";
		cout<< endl; 
		exit(1);
	}


	
	int N, t, tmax;
	N = atoi(argv[1]);
	tmax = atoi(argv[2]);
	size_t n_l = N; 
	size_t n_r = 0;
	srand(time(0));  // initialize seed for RNG

	outfile.open("out.txt");
	
	for(t = 0; t < tmax; t++ ) {
		double p_l = ( (double) n_l)/((double) N); 
		double x = ((double) rand())/((double) RAND_MAX);
		//cout<<"x = "<<x<<endl;  
		//cout<<"p_l = "<<p_l<<endl; 
		if(x <= p_l) { n_l -= 1; n_r += 1; }
		else {n_l += 1; n_r -= 1; }
		outfile << setiosflags(ios::showpoint) ;
		outfile << setw(10) << t; 
		outfile << setw(10) << n_l;
		double exact = ((double) N)/2. * (1+ exp(-2.*t/((double) N))) ;
		outfile << setw(10) << exact<<endl; 
	}

	cout<<"Results in out.txt" << endl;
	return 0;

} // end main

double std_dev(double data[], int size, double avg = 0){ 
	double sum = 0; 
	
	if (avg == 0) {
		for(int i = 0; i< size; i++ ) sum += data[i];
		avg  = ((double)  sum)/((double) size);
	}

	double stdev = 0;
	for(int i = 0; i< size; i++) stdev += pow((data[i]-avg),2);
	stdev = sqrt(stdev/size);
	return stdev;
}

