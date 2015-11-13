#include "Lattice.h"
#include<iostream>
#include"TProfile.h"
#include"TFile.h"
#include<vector>
#include"methods.h"
#include<random>
#include<ctime>
using namespace std; 

const int numWindows = 100; 
vector<double> windows; 

int L = 21; 
double T = 2.0; 
double h = 0.0; 
double J = 1.0; 

int numSweeps = 100000 ; 
int numSteps = L*L*numSweeps; 
int numPasses = 1; // 500  
int sampleRate = L*L;// numSteps/1000; 

TProfile * mag ; 
TH1 * magHist[numWindows]; 

TFile * dataFile = new TFile("data_us.root", "recreate"); 
void createHistograms();
void WriteHistograms(); 
int close(); 

int main() { 
	double num_acc = 0; 
	srand(time(0)); 
	int acc; 
	for(int j = 0; j < numWindows; j ++ ) { 
		double wi = -1 + 2 * j /(float) numWindows ;
		//cout<< wi << endl ; 
		windows.push_back(wi); 
	}

	createHistograms();
	
	// usage: Lattice ( box length, temp, coupling = 1., field = 0.0)  
	for(int i = 0; i < numWindows; i++) { 
		cout << "window " << i << endl;
		double wmin, wmax; 
		wmin = windows[i] ; 
		if ( i + 1 < numWindows) wmax = windows[i+1] ; 
		else wmax = 1.; 
		wmin -= (i != 0 ) ? 1./400 : 0. ;  
		
		for(int p = 0; p < numPasses; p++ ) { 
			Lattice * system = new Lattice(L,T,J,h) ; 
		
			float target = 2.;
			while (fabs(target) > 1) {
				target = wmin + (wmax-wmin)*rand()/float(RAND_MAX) ; 
			}
			
			cout<<"target: " << target<<endl;
			adjustM(system, target ) ; 
			cout << system->GetM() << endl ; 

				for(int step = 0; step < numSteps; step ++)  { 

					acc = umbrella_mc_step(system, wmin, wmax );
					num_acc += acc/numSteps; 
					//cout<<system->GetM() << endl;
					//magHist[i]->Fill(system->GetM()); 
					if ( step%sampleRate == 0 ) {
						double m = system->GetM() ; 
						magHist[i]->Fill(m);
						//cout << "min: " << wmin << "max: " <<  wmax << "m:  " <<  m << endl ;
					}
				}
			mag->Fill(0.5*(wmin+wmax), magHist[i]->GetMean()); 
		}
		//exit(1); 
	}


	WriteHistograms(); 
	return close(); 
}

void createHistograms() {
	//for(int i = 0; i < 14; i++) cout<<windows[i] << endl; 
	// n is for negative 
	mag = new TProfile("mag_n","mag_n", numWindows-1,&windows[0]);
	
	for (int i = 0; i < numWindows; i++) {
		char name[15];
		sprintf(name,"magHist_%d",i);
		
		double wmin, wmax; 
		wmin = windows[i] ; 
		if ( i + 1 < numWindows) wmax = windows[i+1] ; 
		else wmax = 1.; 
		wmin -= (i != 0 ) ? 1./400 : 0. ;  

		int nbins = (i == 0 ) ? 5 : 6; 
		magHist[i] = new TH1D(name,name,nbins, wmin, wmax); 
		//magHist[i] ->SetBit(TH1::kCanRebin); 
	}
}

void WriteHistograms() {
	mag->Write();
	for(int i = 0 ; i < numWindows; i++) magHist[i]->Write(); 

	for( int i = 0; i < numWindows; i++) {
		char name[15]; 
		sprintf(name, "window_%d",i) ; 
		FILE *outfile = fopen(name, "w") ; 

		int nbins_i = magHist[i] ->GetNbinsX(); 
		double bin_I = magHist[i]->Integral("width") ; 
		if (bin_I > 0 ) {
			magHist[i]->Scale(1./magHist[i]->Integral("width")) ;
		}
		for(int j = 1; j <= nbins_i; j++) {
			char data[50]; 
			sprintf(data,"%f\t%.1f\n", magHist[i]->GetBinCenter(j), magHist[i]->GetBinContent(j)) ; 
			fputs(data, outfile) ;
		}

		//fclose(outfile);  
	}
}

int close() {
		
	dataFile->Close();
	return 0; 
}

//int RunSimulation(int numsteps); 
