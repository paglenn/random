#include<fstream>
#include<iostream>
using namespace std; 

int main() {
	ofstream myfile;
	myfile.open("example.txt");

	myfile << "Hello" << " " << "world" << endl;
	myfile << "Hello" << " " << "world" << endl;
	myfile << "Hello" << " " << "world" << endl;
	myfile << "Hello" << " " << "world" << endl;
	myfile << "Hello" << " " << "world" << endl;

	myfile.close();
	cout<< "done!" << endl;
	return 0;
}
