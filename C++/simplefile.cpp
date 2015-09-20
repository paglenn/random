#include<fstream>
#include<iostream>
using namespace std; 

int main() {

	ofstream outfile; 
	outfile.open("hi.txt"); 
	outfile << "hello"; 
	outfile.close(); 
	return 0; 
}
