/* boltzmann_mc.cpp
 * Author: Paul Glenn
 * show that the Metropolis algorithm generates the 
 * Boltzmann velocity distribution (in one dimension)
 * units: mass = 1, T in units of energy so E ~ v^2 ~ T
 */
#include<iostream>
#include<cstdlib>
#include<ctime>
#include<iomanip>
#include<fstream>
#include<cmath>
using namespace std;

inline double randn() { return ((double) rand())/((double) RAND_MAX); }

inline double bFactor(double delta_E, double T) { 
	double beta = 1./T ; 
	double B =  exp( - beta * delta_E  ); 
	return B; 
}

int main(int argc, char* argv[]) {

	if(argc != 4) { 
		cout<<"Usage: ./a.out [Temperature] [MC_cycles] [v_0]"<<endl;
		return 1;
	}

	double T = atof(argv[1]); 			// read in reduced temperature 
	int  MC_cycles = atoi(argv[2]);		// read in num monte-carlo cycles 
	double v0 = atof(argv[3]) ;			// read in initial vel 

	/*
	cout << "Input the number of MC cycles to use: ";
	cin >> MC_cycles;
	cout << endl; 

	cout<<"Input the initial velocity: ";
	cin >> v0;
	cout<< endl;
	*/
	double v_max = 10*sqrt(T); 
	int N  = 500; 								//number of velocity intervals 
	double v_int = v_max/((double) N) ; 
	double dv = T; //0.25*v_max; 						// velocity step	
	
	//Bins initially denote right endpoint of interval 
	double bin[N], freq[N];		
	
	for(int i = 0; i < N; i++) {
		bin[i] = v_int + i*v_int; 
		freq[i] = 1;
	}
	
	//Time for MC algorithm 
	srand(time(0));
	double v = v0;
	int accepted = 0; 
	double v_avg = 0; 
	for(int i = 0; i< MC_cycles; i++ ) {

		double delta_v = (2*randn() - 1) * dv; 
		double v_new = v + delta_v ;
		double delta_E = 0.5* (pow(v_new,2) - pow(v,2));

		//Acceptance criteria 
		if( delta_E < 0 ) { 
			v = v_new ; 
			accepted += 1;
		}
		else if ( bFactor(delta_E,T) >= randn() ) {
			v = v_new;
			accepted += 1;
		}
		v_avg += v/((double) MC_cycles);

		int j = 0; 
		while(bin[j] < fabs(v)) {j += 1; }
		freq[j] += 1;
		
	}
	double E_final = 0.5 * pow(v,2); 
	double E_t = ((double) T)/2. ; 


	printf("Velocity step: %.3f\n",dv) ;
	printf("Number of MC steps: %.1e\n", (double) MC_cycles);
	printf("Number of accepted steps: %i \n",accepted);
	printf("Average velocity: %.3f (theoretical 0.00)\n",v_avg); 	
	//printf("Final velocity: %.2f\n", v);`
	//printf("Final energy: %.2f (theoretical %.2f)\n", E_final, E_t);
	//printf("Energy error: %.2f\n", abs(E_final - E_t)/E_t) ; 

	// Output simulation results 
	ofstream freq_file, log_file ;
	freq_file.open("mc_boltzmann_dist.txt");
	log_file.open("mc_boltzmann_log.txt");
	
	//Modify bins to average of interval
	bin[0] = bin[0]/2.; 
	for(int i = 1; i < N; i++) bin[i] = (bin[i] + bin[i-1])*0.5;

	int max_freq = *max_element(freq, freq+N);
	double rel_freq[N], boltzmann[N], logP[N] ;
	
	for(int i = 0; i < N; i++) { 
		freq_file<< setw(15) << bin[i] ;

		/* For velocities (not speeds), 
		 * the distribution should simply be 
		 * a decaying exponential 
		 */
		rel_freq[i] = ((double) freq[i] )/((double) max_freq) ;
		freq_file<< setw(15) << rel_freq[i] ;
		
		//Compute boltzmann factor for comparison 
		double E = 0.5*bin[i]*bin[i];
		boltzmann[i] = bFactor(E, T);
		freq_file << setw(15) << boltzmann[i] ;
		
		
		/* Test of the qualitative accuracy: 
		 * A plot of -log P vs v^2 should yield 
		 * a straight line with slope (2T)^-1
		 */
		log_file<< setw(15) << bin[i]*bin[i] ;
		logP[i] = - log(freq[i]) ;
		log_file<< setw(15) << logP[i] ;


		freq_file << endl;
		log_file << endl; 
	}
	double approx_slope = (logP[N/5] - logP[N/5-1])/(bin[N/5]*bin[N/5] - bin[N/5-1]*bin[N/5-1]) ;  
	printf("Approximate slope of -log(P) vs v^2: %.3f \n",approx_slope);
	printf("Slope error: %.1f%%\n", abs (approx_slope - 1/((double) T*2) )*2*T*100 ) ; 
	//	

}// end main 

	


	
