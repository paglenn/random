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
	/*	
	cout<< "Input number of particles "; 
	cin >> N;
	cout<<endl;
	
	cout<<"Input number of timesteps: ";
	cin >> tmax; 
	cout<<endl; 
	*/
	size_t n_l = N; 
	size_t n_r = 0;
	srand(time(NULL));  // initialize seed for RNG

	outfile.open("out.txt");
	//outfile << setw(10) << "time";
	//outfile << setw(10) << "n_l";
	//outfile << setw(10) << "error"<< endl;
	
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
		//double arr[1] = {n_l};
		//outfile << setw(10) << std_dev(arr,1,N/2.)<< endl;
	}

	//printf("n_l = %d \n n_r = %d \n",n_l, n_r);
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

