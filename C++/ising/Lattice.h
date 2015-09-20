// Lattice.h 
// Ising model MCMC program 
// By Paul Glenn
#include<iostream>
#include<cmath> 
#include<random>
#include<vector>
#include<ctime>

using std::vector; 
using std::cout; 
using std::endl; 

#ifndef LATTICE_H_
#define LATTICE_H_

class Lattice { 
	// an LxL (Ising) lattice 

	int L , numSites ;
	double h, J ; // reduced coupling constants  
	int seed;  
	double M ; // magnetization
	vector<double> S;	// lattice sites  

	public: 
	
		double T, beta ; 

		Lattice(int sideLength, double temp, double coupling, double field) ; 

		double GetE(); // total dimensionless energy of lattice 

		int  GetRandomSite(); // random site index for mc step 

		int GetSite(int index); // return value of spin at site  

		vector<int> neighborList(int index); //list of nearest neighbors 

		int GetN(); // number of lattice sites 

		double GetH(); // field variable 

		double GetJ(); // exchange constant (reduced) 

		void FlipSpin(int index);  

		double GetM(); // magnetization per spin 


};

Lattice::Lattice(int sideLength, double temp, double coupling = 1.0, double field = 0.0 ) : 
	L(sideLength), J(coupling), h(field) , T(temp) 
{

	seed = time(0); 
	srand(seed); 

	numSites = L * L; 
	beta = 1./T; 
	M = 0.; 
	for(int i = 0; i < numSites; i++) 
	{
		S.push_back(2*(rand()%2)-1) ; 
		//S.push_back(1) ; 
		//S.push_back(-1); 
		M += S[i]; 
	}


}

int Lattice::GetSite(int index) { return S.at(index); } 

double Lattice::GetH() {return h; }

double Lattice::GetJ() {return J; }

double Lattice::GetM() { 
	return M/numSites; 
}

void Lattice::FlipSpin(int index) { 
	S.at(index)  *= -1 ; 
	M += 2*S.at(index);  
}

std::vector<int> Lattice::neighborList(int index ) { 
	int nbr[4]; 
	nbr[0] = (index + 1)%numSites; 
	nbr[1] = (numSites + index -1)%numSites ; 
	nbr[2] = (index + L)%numSites; 
	nbr[3] = (numSites + index - L) %numSites ; 
	std::vector<int> nbrs ; 
	for(int i = 0; i < 4; i++) nbrs.push_back(nbr[i] ); 
	return nbrs; 
}

double Lattice::GetE() {
	// calculate dimensionless energy beta * E 

	double E = 0;

	for(int i = 0; i < numSites ; i ++) {

		vector<int> nbrs = neighborList(i); 

		for(int j = 0; j < nbrs.size(); j++) {
			
			E -= 0.5 * J * S[i] * S[nbrs[j]]; 
		} 

		E -= h * S[i]; 
	}

	return beta * E; 
}

int Lattice::GetRandomSite() {
	// random lattice index 
	return rand()%numSites; 
}

int Lattice::GetN() { return numSites; } 

#endif 
