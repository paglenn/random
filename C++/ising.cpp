#include<iostream>
#include<cmath>
#include<iomanip>
#include<fstream>
//#include<TH1D.h>
#include<vector>
#include<random>
#include<ctime>

const int L = 20; 
int T = 2; 

//nearest neighbors with PBC's 
std::vector<int> neighborList(int i); 

int main() { 

	for(int i = 0; i < 4; i++) std::cout<< neighborList(20)[i] << std:: endl; 
	return 0; 
	
}

std::vector<int> neighborList(int i ) { 
	int nbr[4]; 
	int N = L*L; 
	nbr[0] = (i + 1)%N; 
	nbr[1] = (N + i -1)%N ; 
	nbr[2] = (i + L)%N; 
	nbr[3] = (N + i-L) %N ; 
	std::vector<int> nbrs ; 
	for(int i = 0; i < 4; i++) nbrs.push_back(nbr[i] ); 
	return nbrs; 
}

class Lattice { 
	const int size; 
	int sites[size];

	Lattice(const sideLength ) : size(sideLength) {}

	public: 
		
		
		

}

void 


	

