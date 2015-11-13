// Methods complementary to lattice ising program 
// 
#include<vector>
#include"Lattice.h"
#include<iostream>
#include<cmath>


double deltaE(Lattice* system, int index) {

	double dE = 0 ;
	vector<int> nbrs = system->NeighborList(index); 
	int s_ij = system->GetSite(index);  

	for(int i = 0; i < nbrs.size(); i++) {

		dE += 2 * system->GetJ() * s_ij *system->GetSite(nbrs[i]); 
	}

	dE += 2 * s_ij * system->GetH(); 

	return dE * system->beta; 
}

double ranf() { return rand()/(float) RAND_MAX ; }

bool mc_step(Lattice* system) {

	int random_index = system->GetRandomSite(); 
	//cout<<"index: " <<random_index<<endl;

	double dE = deltaE(system, random_index) ; 
	
	bool accepted = false; 
	if (dE <= 0) accepted = true; 
	else if ( ranf() <= exp(-dE ) ) accepted = true; 

	if (accepted) system->FlipSpin(random_index) ; 

	return accepted; 

}

void adjustM(Lattice * system, double target, double tol = 1./100) {

	double m = system->GetM(); 
	//std::cout << "adjusting: " << std::endl;
	while ( fabs(m - target) > tol) {
		double s ;
		bool delta = false; 

		if ( m > target) s = 1; 
		else s = -1; 

		int random_site = system->GetRandomSite(); 
		if ( system->GetSite(random_site) == s ) delta = true;  // signifies acceptance 
		
		// this way, the rather expensive calculation of the magnetization is only done if a 
		// flip actually happened. 
		if ( delta ) {
			system->FlipSpin(random_site) ;  
			m = system->GetM(); 
		}
		//std::cout <<"target " << target << std::endl; 
		//std::cout << "m: " << m << std::endl; 
	}
	//std::cout<< " accepted " << std::endl;
}

double V_bias(double m , double wmean) { 

	double K = 40.0 ; 
	double diff = m - wmean ; 
	return 0.5 * K * diff * diff ; 

}

bool umbrella_mc_step(Lattice* system, double wmin, double wmax ) {

	int random_index = system->GetRandomSite(); 
	double wmean = 0.5 * (wmin + wmax ) ; 
	double m0 = system->GetM() ; 
	double Vold = V_bias( m0, wmean ) ; 

	double dE = deltaE(system, random_index) ; 
	double m_new = m0 - 2 * system->GetSite(random_index) ; 
	double Vnew = V_bias(m_new, wmean) ;  
	
	dE += (Vnew - Vold) ; 
	bool accepted = false; 
	if (dE <= 0) accepted = true; 
	else if ( ranf() <= exp(-dE ) ) accepted = true; 

	if (accepted ) system->FlipSpin(random_index) ; 


	return accepted; 

}

