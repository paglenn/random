// Designed to overflow 
#include <iostream>
#include<cmath>
using namespace std;

int main()
{
	int int1, int2, int3;

	cout<<"Read in the exponential N for 2^N =\n" ; 
	cin>> int2;
	int1 = (int) pow(2., (double) int2);
	cout<<"2^N * 2^N = "<< int1*int1<<endl;
	int3 = int1 - 1;
	cout << "2^N * (2^N - 1) = "<< int1*int3 << endl;
	cout << "(2^N - 1) = "<< int3 << endl;
	return 0;
}
// end main 
