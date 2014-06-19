//HJ Computational Physics p. 195
#include<iostream>
#include<cmath>
#include<iomanip>
#include<fstream>
using namespace std; 

inline int PBC(int i, int limit, int add) {
	return (i+limit+add)%limit;
}

//data from screen (I will change to CLI?)
void read_input(int& , int&, double&, double&) ;
//initialize energy and magnetization 
void initialize(int, double, int **, double&, double& );
// implement Metropolis algorithm
void Metropolis (int , long&, int **, double&, double&, double * ) ;
// Output results to file 
void output ( int , int , double , double *) ;

int main(int argc, char* argv[]) {}
