#include "Lattice.h"
#include<iostream>
#include"TProfile.h"
#include"TFile.h"
#include<vector>
#include"methods.h"
using namespace std; 

//double Tvals[14] = {0.1,1.0,1.5,2.0,2.1,2.15,2.2,2.269,2.3,2.35,2.4,3.0,4.0,5.0}; 
const int nT = 50; 
vector<double> Tvals; 

int L = 20; 
double h = 0.0; 
double J = 1.0; 

int numSweeps = 1e4; 
int numSteps = L*L*numSweeps; 
int sampleRate = L*L;// numSteps/1000; 

TProfile * mag ; 
TH1 * magHist[nT]; 

TFile * dataFile = new TFile("data_temp.root", "update"); 
void createHistograms();
void WriteHistograms(); 
int close(); 

int main() { 
	double num_acc = 0; 
	int acc; 
	for(int j = 0; j < nT; j ++ ) { 
		double T = 0.1 + j * (4 - 0.1)/ nT; 
		Tvals.push_back(T); 
	}

	createHistograms();
	
	// usage: Lattice ( box length, temp, coupling = 1., field = 0.0)  
	for(int i = 0; i < nT; i++) { 
		double T = Tvals[i] ; 
		for (int j = 0; j < 10; j++) {
			Lattice * system = new Lattice(L,T,J,h) ; 

			for(int step = 0; step < numSteps; step ++)  { 

				acc = mc_step(system);
				num_acc += acc/numSteps; 
				//cout<<system->GetM() << endl; 
				if ( step%sampleRate == 0 ) magHist[i]->Fill(system->GetM());
			}
			mag->Fill(T, magHist[i]->GetMean()); 
		}
	}


	WriteHistograms(); 
	return close(); 
}

void createHistograms() {
	//for(int i = 0; i < 14; i++) cout<<Tvals[i] << endl; 
	// n is for negative 
	mag = new TProfile("mag_n","mag_n", nT-1,&Tvals[0]);
	
	for (int i = 0; i < nT; i++) {
		char name[15];
		sprintf(name,"magHist_%d",i);
		magHist[i] = new TH1D(name,name, L*L/2, -1, 1); 
		magHist[i] ->SetBit(TH1::kCanRebin); 
	}
}

void WriteHistograms() {
	mag->Write();
	for(int i = 0 ; i < nT; i++) magHist[i]->Write(); 
}

int close() {
		
	dataFile->Close();
	return 0; 
}







//int RunSimulation(int numsteps); 
