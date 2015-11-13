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
	vector<double> S;	// lattice sites  

	public: 
	
		double T, beta ; 
		Lattice(int sideLength, double temp, double coupling = 1.0, double field = 0.0 ) : 
			L(sideLength), J(coupling), h(field) , T(temp) 
		{

			seed = time(0); 
			srand(seed); 

			numSites = L * L; 
			beta = 1./T; 
			for(int i = 0; i < numSites; i++) 
			{
				S.push_back(2*(rand()%2)-1) ; 
				//S.push_back(1) ; 
				//S.push_back(-1); 
			}
			
		}
		double GetE(); // total dimensionless energy of lattice 

		int  GetRandomSite(); // random site index for mc step 

		int GetSite(int index); // return value of spin at site  

		vector<int> NeighborList(int index); //list of nearest neighbors 

		int GetN(); // number of lattice sites 

		double GetH(); // field variable 

		double GetJ(); // exchange constant (reduced) 

		void FlipSpin(int index);  

		double GetM(); // magnetization per spin 


};

int Lattice::GetSite(int index) { return S.at(index); } 

double Lattice::GetH() {return h; }

double Lattice::GetJ() {return J; }

double Lattice::GetM() { 
	double m = 0.; 
	for(int i = 0; i < numSites; i++ ) m += S.at(i); 
	m /= numSites;
	return m;
}

void Lattice::FlipSpin(int index) { S.at(index)  *= -1 ; }

std::vector<int> Lattice::NeighborList(int index ) { 
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
	// calculate dimensionless energy 

	double E = 0;

	for(int i = 0; i < numSites ; i ++) {

		vector<int> nbrs = NeighborList(i); 

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
