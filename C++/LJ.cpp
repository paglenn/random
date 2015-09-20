#include<iostream>
#include<random> 
#include<fstream>
#include<vector>
#include<iomanip>
using namespace std; 

int main() { 

	ifstream infile; 
	vector<double> coords[3]; 
	infile.open("coordinates.txt"); 
	std::setw(15); 

	for(int i = 0; i < 1000; i++) { 
		double x_i, y_i, z_i; 
		infile >> setw(10) >> x_i ; 
		infile >> setw(10) >> y_i ;
		infile >> setw(10) >> z_i ; 
		infile.ignore(); 
		if ( infile.eof() ) break; 
	
		coords[0].push_back(x_i) ; 
		coords[1].push_back(y_i) ; 
		coords[2].push_back(z_i) ; 
	}

	// compute pair potentials 
	int numParticles = coords[0].size(); 
	double dx, dy, dz, r2, r6, r12, u_ij, f_x, f_y, f_z, U ; 
	cout << setw(15) << "U " << setw(15)  << "f_x"<< setw(15) << "f_y" << setw(15) << "f_z" << endl;
	for( int i = 0; i < numParticles ; i++ ) {
		f_x = 0; f_y = 0.; f_z = 0. ; U = 0.; 
		for ( int j = 0 ; j < numParticles; j++) { 
			
			if (j == i ) continue; 
			dx = coords[0][i] - coords[0][j] ; 
			dy = coords[1][i] - coords[1][j] ; 
			dz = coords[2][i] - coords[2][j] ; 
			r2 = dx*dx + dy*dy + dz*dz ;  
			r6 = r2*r2*r2 ; 
			r12 = r6*r6 ; 
			u_ij = 4*( 1./r12 - 1./r6) ; 
			double m = 24*( 2./r12 - 1./r6) ; 
			f_x  += m * dx/r2 ; 
			f_y  += m * dy/r2 ; 
			f_z  += m * dz/r2 ; 
			U += u_ij; 
		}
		cout << setw(15) << U << setw(15) << f_x << setw(15) << f_y << setw(15) << f_z << endl;
	}



}



