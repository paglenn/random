#include<iostream>
#include<cmath>
#include<cstdlib>
#include<random>
#include<ctime>
#include<vector>
using namespace std; 
// a genetic algorithm for finding the roots of a quadratic.
// may seem like overkill for this problem, but is a nice illustration of 
// the method. 

int x[8][3] = { {0,0,0},{0,1,0},{1,0,0},{0,0,1},{0,1,1},{1,1,0},{1,0,1},{1,1,1}};
int y[3][3];
int randint() { return rand()%8; }

int map_x(int x[3]) {
	int sum = x[0] + 2*x[1] + 4*x[2]; 
	return sum; 
}

double f(int x) { 
	return -x*x + 8.*x + 15.; 
}

// fitness function 
double FF(int index) {
	double sum = 0.;
	for (int i = 0; i < 8; i++) {
		sum += f(map_x(x[i])) ; 
	}
	return f(map_x(y[index]))/sum; 
}

void mutate(int index) {
	int pos = rand()%3; 
	y[index][pos] = 1 - y[index][pos]; 
}

void crossover(int i, int j) { 
	int pos = rand()%3; 
	int old_yip = y[i][pos]; 
	y[i][pos] = y[j][pos]; 
	y[j][pos] = old_yip	 ; 
}

void init() {
	
	for(int i = 0; i < 3; i++)  {
		int j = randint(); 
		y[i][0] = x[j][0] ; 
		y[i][1] = x[j][1] ; 
		y[i][2] = x[j][2] ; 
	}
	
}

	

// mutation 


int main() {
	init(); 

	for(int i = 0 ; i < 10; i++) {
		double fitness[3] ;
		for(int j = 0; j < 3; j++) fitness[j] = FF(j);
		for(int j = 0; j < 3; j++) cout<<fitness[j]<<endl;
		double p_mut = 0.02; 
	}

}


