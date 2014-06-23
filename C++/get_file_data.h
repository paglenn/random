/* get_file_data.h
 * Read in data from a specified column of a text file with specified delimiter
 * has the advantage of not *forcing*  namespace std on user. 
 */

#include<vector>
#include<iostream>
#include<fstream>
#include<string>
#include<cstdlib>

std::vector<double> get_file_data(std::string filename, int col,char delim) {

	std::vector<double> myvec;
	std::string line;
	std::ifstream infile ; infile.open(filename.c_str());
	if(infile.fail() ) {
		std::cout<< "File " << filename << "not found: Abort" << std::endl;
		exit(1);
	}
	while(getline(infile,line)) {
		if (line[0] == '#') continue;
		std::string line2 = " ";
		if( col == 0) {line2 = line; }
		for(int i = 0; i< col; i++)	{
			
			if(line2 == " ") {
				int space = line.find(delim);
				line2 = line.substr(space+1);
			} else {
				int space = line2.find(delim);
				line2 = line2.substr(space+1);
			}

		}
		int space2 = line2.find(delim); 
		std::string final = line2.substr(0,space2);
		double value = atof(final.c_str());
		myvec.push_back(value);
	}

	infile.close();
	/*for(int i = 0; i< myvec.size() ; i++ ) {
		std::cout<<myvec.at(i) << std::endl;
	}*/
	return myvec;
}

