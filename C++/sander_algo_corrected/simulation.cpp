#include "engine.h"
#include<vector>
#include<ctime>
#include<fstream>
using std::cout ;
using std::endl  ;

int main(int argc, char* argv[]) {

	//cout << "Hi there " << endl ; 
	//
	//ofstream ferr ; 
	//ferr.open("errors.dat") ; 
	
	/*
	if (argc < 4 ) { 
		cerr << "usage: ./wlc RP TP RPTP " << endl ; 
		return 0 ; 
	}
	*/
	int start_time = time(0); 
	//double rp_in = atof( argv[1]) ; 
	//double tp_in = atof(argv[2]) ; 
	//double rptp_in = atof(argv[3]) ; 
	double rp_in = 0; 
	double tp_in = 0 ; 
	double rptp_in = 0 ;


	init(); 
	adjustTP(tp_in) ; 
	adjustRP(rp_in) ; 
	
	char progress[75] ; 
	alignRPTP(rptp_in) ;

	double pct_acc = 0; 
	sprintf(progress, "RP = %g \t TP = %g \t RPTP = %g \n", getRP(),getTP(),getRPTP() ) ; 
	fputs(progress,progressFile) ;



	int blockLength; 
	for(int j = 0; j < numSweeps; j++) { 

		// decide resolution 
		if(j == 0) {
			blockLength = equilibrationTime;  
		}	else { 
			blockLength = sampleRate; 
		}
		
		// carry out a block of steps before recording data 
		for(int i = 0 ; i < blockLength; i++) {
			int acc = mc_step(); 
			pct_acc += acc / (float) sampleRate ; 
		}
		
		
		WriteEventData(j);	
		
		
		// Write progress report 
		if(j%progressRate == 0 ) { 
			
			sprintf(progress,"step %g/%g\n", (float) j , (float) numSweeps);
			fputs(progress,progressFile);
			//cout << "step: " << j << endl ; 
			//cout << getRP() << endl ; 
			//ferr << fabs((getRP() - RP)) << endl ;
		}
		
		checkNorms(); 

	} // end simulation 


	// write statistics and close up 
	writeHistograms();
	writeLogFile();  // REQ: write this after hist file 
	
	sprintf(progress, "Z = %g \t RP = %g \t TP = %g \t RPTP = %g\n", getZ() ,getRP(),getTP(),getRPTP() ) ; 
	fputs(progress,progressFile) ;

	char summary[70];
	int end_time = time(0); 
	double tdiff = (end_time - start_time)/float(60); // simulation time in minutes  
	pct_acc = pct_acc / (double) numSweeps; 
	sprintf(summary,"%.2f%% steps accepted\nrunning time: %.2f minutes\n",100*(pct_acc),tdiff);
	fputs(summary,progressFile); 

	sprintf(summary,"zmax: %.2f", z_mp ) ; 

	//ferr.close();
	return cleanup(); 
}



