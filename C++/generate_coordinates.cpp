#include<iostream>
#include<random> 
#include<fstream>
#include<vector>
#include<iomanip>
using namespace std; 

void generate_coordinates(int num_points, double boxSize ) {
	double sigma = 1.; 
	ofstream outfile; 
	if (argc <= 1) { 

		cerr << " usage: ./a.out num_points boxSize" << endl; 
		return 1; 
	}

	numPoints = atoi(argv[1]) ; 
	boxSize = atoi(argv[2]) ; 
	bool is_good = false; 


	srand(time(0)) ; 
	while ( !is_good ) { 
		vector<double> positions[3]; 

		for ( int i = 0 ; i < numPoints; i ++ ) { 

			float x_i = boxSize * ( 2.*rand() / (double) RAND_MAX  -1.) ; 
			float y_i = boxSize * ( 2.*rand() / (double) RAND_MAX  -1.) ; 
			float z_i = boxSize * ( 2.*rand() / (double) RAND_MAX  -1.) ; 

			positions[0].push_back(x_i) ; 
			positions[1].push_back(y_i) ; 
			positions[2].push_back(z_i) ; 
		}

		bool collision = false; 
		for ( int i = 0; i < numPoints; i ++) { 
			if (collision) break; 
			for ( int j = i+1 ; j  < numPoints; j++ ) { 
				double dx = positions[0][i]  - positions[0][j];
				double dy = positions[1][i]  - positions[1][j];
				double dz = positions[2][i]  - positions[2][j];

				collision = dx*dx + dy*dy + dz*dz < sigma*sigma  ; 
				//cout << dx * dx + dy * dy + dz * dz<< endl; 
				//cout << collision << endl; 
				
				if (collision) break; 
			}
		}
		
		if ( !collision) {




			for (int i = 0; i < numPoints; i++ ) { 

				int islot = 3*i ; 
				R[islot] = positions[0][i] ; 
				R[islot+1] = positions[1][i] ; 
				R[islot+2] = positions[2][i] ; 


			}
			is_good = true; 
		}
	}






}
int main(int argc, char* argv[] ) { 

	int numPoints; 
	int boxSize; 
	double sigma = 1.; 
	ofstream outfile; 
	if (argc <= 1) { 

		cerr << " usage: ./a.out num_points boxSize" << endl; 
		return 1; 
	}

	numPoints = atoi(argv[1]) ; 
	boxSize = atoi(argv[2]) ; 
	bool is_good = false; 


	srand(time(0)) ; 
	while ( !is_good ) { 
		vector<double> positions[3]; 

		for ( int i = 0 ; i < numPoints; i ++ ) { 

			float x_i = boxSize * ( 2.*rand() / (double) RAND_MAX  -1.) ; 
			float y_i = boxSize * ( 2.*rand() / (double) RAND_MAX  -1.) ; 
			float z_i = boxSize * ( 2.*rand() / (double) RAND_MAX  -1.) ; 

			positions[0].push_back(x_i) ; 
			positions[1].push_back(y_i) ; 
			positions[2].push_back(z_i) ; 
		}

		bool collision = false; 
		for ( int i = 0; i < numPoints; i ++) { 
			if (collision) break; 
			for ( int j = i+1 ; j  < numPoints; j++ ) { 
				double dx = positions[0][i]  - positions[0][j];
				double dy = positions[1][i]  - positions[1][j];
				double dz = positions[2][i]  - positions[2][j];

				collision = dx*dx + dy*dy + dz*dz < sigma*sigma  ; 
				//cout << dx * dx + dy * dy + dz * dz<< endl; 
				//cout << collision << endl; 
				
				if (collision) break; 
			}
		}
		
		if ( !collision) {

			outfile.open("coordinates.txt") ; 

			for (int i = 0; i < numPoints; i++ ) { 

				outfile << setw(15) << positions[0][i] ; 
				outfile << setw(15) << positions[1][i] ; 
				outfile << setw(15) << positions[2][i] ; 
				outfile << endl; 
			}
			outfile.close(); 
			is_good = true; 
		}
	}

}

