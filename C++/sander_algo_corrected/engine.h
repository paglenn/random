#include<iostream>
#include<cassert>
#include<cmath>
#include<math.h>
#include<vector>
#include<string>
#include<cstdlib>
#include<ctime>
#include"VectorMethods.h"
#include<cstring>
#include "MersenneTwister.h"
#include<fstream>
#include<iomanip>
#include"Mathematx.h"
using std::vector; 
using std::endl; 
using std::cout; 
using std::cerr; 
using std::ofstream;
using std::setw;

// system parameters 
double L,_L,ds, _ds, _N , _Nm2; 
int N; 
vector<long double> tx, ty, tz, tox,toy,toz ; 
vector<long double> psi, phi, ophi, opsi ;  
long double tx_new , ty_new, tz_new ;  
double xi ,yi,zi ; 
double tp[2], rp[2] ; 
double urn; 
long double norm2; 
long double snorm2, _snorm2;
double zmax ; 
double z_mp ;

// simulation parameters 
int numSweeps, numSteps; 
int numPasses, numWindows, numFrames; 
int sampleRate, progressRate, equilibrationTime; 
int nbins ; 
double binWidth, binOverlap; 
double astep, bias ; 
vector<double> winMin, winMax, zmin,K ; 
double zstart, wmax,wmin,width, wmean, z ;
double target, tol;
int random_index ;
int totalCounts; 

const int nMoments = 2; 
double zMoments[nMoments]; 

double thetaMax ; 
double r2; 
double sx, sy; 
double ans; 


// hard conditions on certain variables
bool flag ; 
double RP, TP, RPTP ; 

// Data files 
FILE * inFile; 
FILE * zFile;
FILE * progressFile; 
FILE * metaFile; 
vector<FILE*> windowFiles; 
vector<FILE*> histFiles; 
vector< vector<double> > zHists; 
vector<double> cosHist; 
int rmax = 15 ;
vector<double> corr(rmax,0.0); // for average correlator  
vector<int> TC_corr(rmax,0); // for total counts  
ofstream fout ; 
ofstream coorFile ; 

//ofstream zFiles[20];

//const long double PI = acos(-1.0);
const double sqrt2 = sqrt(2) ; 
const double eps = 1e-4; // for singular things or comparison 
int iseed ; 
//std::mt19937 rng; 
MTRand rng; 


void readInParameters() {

	inFile = fopen("parameters.txt","r"); 
	if (inFile == NULL) { 
		cerr << "parameter file not found!" << endl; 
		exit(1); 
	}

	while(!feof(inFile)) {
		char str[100]; 
		fscanf(inFile,"%s",str);
		if ( *str == '#')  fgets(str,100,inFile) ; 
		else if ( *str == 'L') fscanf(inFile,"%lf",&L);
		else if ( *str == 'N') fscanf(inFile,"%d", &N); 
		else if (!strcmp(str,"numSweeps")) fscanf(inFile,"%d",&numSweeps); 
		else if (!strcmp(str,"sampleRate")) fscanf(inFile,"%d",&sampleRate); 
		else if (!strcmp(str,"progressRate")) fscanf(inFile,"%d",&progressRate); 
		else if (!strcmp(str,"equilibrationTime")) fscanf(inFile,"%d",&equilibrationTime); 
		else if (!strcmp(str,"iseed"))	fscanf(inFile, "%d", &iseed ) ;  
		else if (!strcmp(str,"astep")) fscanf(inFile,"%lf",&astep); 
		else if (!strcmp(str,"thetaMax")) fscanf(inFile,"%lf",&thetaMax); 
		else if (!strcmp(str,"numWindows")) fscanf(inFile,"%d",&numWindows); 
		else if (!strcmp(str,"numPasses")) fscanf(inFile,"%d",&numPasses); 
		else if (!strcmp(str,"zstart")) fscanf(inFile,"%lf",&zstart); 
		else if (!strcmp(str,"bias")) fscanf(inFile,"%lf",&bias); 
		else if (!strcmp(str,"nbins")) fscanf(inFile,"%d",&nbins); 
		//else std::////cout<<"whoami" << str<<std::endl;
	}

	// MF correction / rescaling
	cout << L << endl ; 
	_L = 1./L ; 
	L = 1./(_L + 2) ; 
	cout << "Rescaled: " << L << endl ; 
	fclose(inFile) ;
}

/*
bool diff(double a, double b) { 
	// percent difference 
	//if (fabs(a-b)  > eps) return true; 
	if (a == 0 || b ==0 ) { 
		if (fabs(a-b) > eps) return true ; 
	} else { 
		double abs_diff = fabs(a -b ) ;	
		if (abs_diff > 1e-4 ) return true ; 
	}
	return false; 
}

double atan_proper(double x, double y) { 
	double theta ; 
	if (x == 0 ) {
		if (y > 0) theta =  PI/2.0 ; 
		else if (y < 0) theta =  PI/2.0 ; 
	} else {
		theta = atan(y/x ) ; 
		if(x > 0 and y > 0 ) {
			theta = theta ; 
		} else if (x > 0 && y< 0) {
			theta = theta + 2*PI ; 
		} else {
			theta = theta + PI ; 
		}
	}
	return theta ; // never runs 
}
*/
void checkNorms() { 
	// enforce normality of the t_i to within 1e-4 %  
	for(int i = 1; i +1 < N; i++) {
		norm2 = tx.at(i)*tx.at(i) + ty.at(i)*ty.at(i) + tz.at(i)*tz.at(i) ; 
		if(diff(norm2,1.0)) {
			cerr << " vector " << i << "failed to be normal " << std::endl; 
			cerr << "instead has magnitude " << norm2  << endl;
			exit(1); 
		}
	}
}

double innerProduct(double x1, double y1, double z1, double x2, double y2, double z2) {
	ans = x1*x2 + y1*y2 + z1*z2; 
	return ans; 
}


void createHistograms() {

	totalCounts = 0 ; 
	for(int i = 0.; i < numWindows; i++) {
		zHists.push_back( vector<double>(nbins, 0.0) ) ; 
	}
	cosHist = vector<double>(nbins,0.0) ; 
}

void normalize(int index) {

	norm2  = tx.at(index)*tx.at(index) + ty.at(index)*ty.at(index) + tz.at(index)*tz.at(index) ;  
	long double _norm = 1./sqrt( (long double) norm2) ; 
	tx.at(index) *= _norm; 
	ty.at(index) *= _norm; 
	tz.at(index) *= _norm; 

}

double getZ() {
	// height of polymer along z-axis  
	double zsum  = 0.;
	for(int j = 0; j < N; j++) zsum += tz.at(j) ;
	assert(!isnan(zsum)) ;
	return zsum * _N; 
}

double getRP() {
	// projection of eed vector into the plane 
	//double ans = sqrt( rp[0]*rp[0] + rp[1]*rp[1]) ; 
	//return ans/ (float) N ; 

	long double rpf = 0.0;  
	sx = 0.0 ; sy = 0.0 ;  
	for(int i = 1 ; i < N ; i++) { 
		sx += tx.at(i) ; 
		sy += ty.at(i) ; 
	}

	rpf = sqrt(sx*sx + sy*sy ) ;
	return rpf * _N ; 
}

double getTP() { 
	//perpendicular component of final segment 
	ans = sqrt(tx[N-1]*tx[N-1] + ty[N-1]*ty[N-1]);
	return ans ; 
}

double getRPTP() {
	// innerProduct product of perpendicular component of final segment and 
	// projection of eed vector into the plane 
	sx = 0.0 ; sy = 0.0 ;  
	for(int i = 1 ; i < N ; i++) { 
		sx += tx.at(i) ; 
		sy += ty.at(i) ; 
	}

	return (sx*tp[0] + sy*tp[1])* _N ; 
}


double ranf() { 

	double u = 10;
	while(u >= 1 || u < eps ) u = rng.rand() ;
	return u ; 
}


void init() {

	readInParameters();
	//	std:://cout<<"Initialized" << std::endl;
	//
	_N = 1./N ; 
	ds = L * _N ; 
	_ds  = 1./ds; 
	numSteps = numSweeps * N; 
	////cout << numSteps << endl ;
	numFrames = numWindows * numPasses * numSteps ; 
	binWidth = (1. - zstart)/nbins; 
	binOverlap = 1 * binWidth; 
	rng.seed(); 

	zFile = fopen("uwham.dat","w");

	progressFile = fopen("progress.out","w"); 
	if ( progressRate > numFrames/1000 ) progressRate = numFrames / 1000 ; 

	tx.assign(N,0.); 
	ty.assign(N,0.); 
	tz.assign(N,1.);
	tox.assign(N,0.); 
	toy.assign(N,0.); 
	toz.assign(N,1.);
	psi.assign(N,1.) ; 
	phi.assign(N,0.) ;
	opsi.assign(N,1.0) ; 
	ophi.assign(N,0.0) ;
	tp[0] = tp[1] = 0.0 ; 
	rp[0] = rp[1] = 0.0 ; 


	char fileName[15]; 
	sprintf(fileName,"window.dat"); 
	windowFiles.push_back(fopen(fileName,"w")); 

	sprintf(fileName,"hist.dat"); 
	histFiles.push_back(fopen(fileName,"w")); 
	zmax = 0.0 ; 

	//coorFile.open("coor.xyz") ; 
	createHistograms(); 
}

void savestate() {

	for(int index = 0 ; index < N; index++) {
		tox.at(index) = tx.at(index); 
		toy.at(index) = ty.at(index); 
		toz.at(index) = tz.at(index); 
		ophi.at(index) = phi.at(index) ; 
		opsi.at(index) = psi.at(index) ; 
	}
}
double V_bias(double z, int wj ) { 
	return 0.5*K[wj]*pow(z - zmin[wj], 2.);
}

int perturb(int ip, int jp ) { 

	//cout << "phi " << phi.at(ip) << endl ;
	//cout << "phi " << phi.at(jp) << endl ;
	int OK = 1 ; 
	long double rx, ry ; 
	long double dir1, dir2 , dpsi, dphi ; 
	rx = tx.at(ip) + tx.at(jp) ; 
	ry = ty.at(ip) + ty.at(jp) ; 

	dir1 = rng.rand() - 0.5 ; 
	dir2 = rng.rand() - 0.5 ;  

	dpsi = dir1 * astep ; 
	dphi = dir2 * thetaMax; 

	psi.at(ip) += dpsi ; 
	phi.at(ip) += dphi ;
	//cout << phi.at(ip) << " " << psi.at(ip) << endl ;
	if (std::abs( psi.at(ip)) > 1) OK = 0 ;

	if(OK){
		long double sp, st, cp , ct ; 
		sp = sin(phi.at(ip)) ; 
		cp = cos(phi.at(ip)) ; 
		ct = psi.at(ip) ; 
		st = sqrt( 1 - ct * ct ) ;
	//	cout << "stcpi" << st * cp  << endl ; ;

		tx.at(ip) = cp * st ;
		ty.at(ip) = sp * st; 
		tz.at(ip) = ct; 

		urn = rng.rand() - 0.5 ; 

		long double drx, dry, drx2, dry2 , dr2 ; 
		drx = rx - tx.at(ip) ; 
		drx2 = drx * drx ; 
		dry = ry - ty.at(ip) ; 
		dry2 = dry * dry ; 

		phi.at(jp) = atan_proper(drx,dry) ; 

		dr2 = drx2 + dry2 ;  	
		if (dr2 > 1 ) OK = 0  ;  

		if (OK) { 
			psi.at(jp) = sgn(urn) * sqrt(1.0 - dr2 ); 
			sp = sin(phi.at(jp)) ; 
			cp = cos(phi.at(jp)) ; 
			ct = psi.at(jp) ; 
			st = sqrt( 1.0 - ct * ct ) ;
			tx.at(jp) = cp * st ;
			ty.at(jp) = sp * st; 
			tz.at(jp) = ct; 
		}
	}
	//rx = tx.at(ip) + tx.at(jp) ; 
	//ry = ty.at(ip) + ty.at(jp) ; 
	//cout << "after: " << getRP( ) << endl ; 
	//cout << "rxa " << rx << endl ;
	//cout << "rya " << ry << endl ;
	//if(OK) exit(1);
	return OK ; 
}

double getE()  { 
	double E = 0. ; 
	for ( int i = 0; i+1 < N; i++) {
		E -= tx.at(i)*tx.at(i+1) + ty.at(i) * ty.at(i+1) + tz.at(i) * tz.at(i+1) ; 
	}
	return _ds * E ; 
}

double revert(int index) {


	tx.at(index) = tox.at(index); 
	ty.at(index) = toy.at(index); 
	tz.at(index) = toz.at(index); 

	phi.at(index) = ophi.at(index) ; 
	psi.at(index) = opsi.at(index) ; 

	return 0 ; 

}

void revert() { 
	for(int i = 1 ; i+1 < N ; i++) {
		revert(i); 
	}
}



bool conditional_check() {  
	bool ans = false  ; 
	ans = ans || diff(RP,getRP()) ; 
	ans = ans || diff(TP,getTP()) ; 
	ans = ans || diff(RPTP, getRPTP()) ; 
	return ans ; 

}

void rotate_T(double angle, int dim = 3) {
	////cout << "Angle " << angle << endl ; 

	vector<double> v(3,0.); 
	v[0] = tx[N-1] ; 
	v[1] = ty[N-1] ; 
	v[2] = tz[N-1] ; 
	//double norm2 = tx[N-1]*tx[N-1]  + ty[N-1] *ty[N-1] ; 
	//if (dim == 3) v = rotate_phi(v,angle) ;
	v = rotate_2D(v,angle) ; 

	//update RP 

	tx[N-1]  = v[0] ; 
	ty[N-1]  = v[1] ; 
	tz[N-1]  = v[2] ; 
	//norm2 = tx[N-1]*tx[N-1]  + ty[N-1] *ty[N-1] ; 

	tp[0] = tx[N-1] ; 
	tp[1] = ty[N-1] ; 

}

void alignRPTP(double target) {
	// target is mapped to an angle between 0 and PI 
	//double tpx = tp[0] ; double tpy = tp[1] ; 
	double norm = RP * TP   ; 
	double theta_0 ; 
	if (norm < eps)  return; 
	else { 
		theta_0 = atan_proper(rp[0],rp[1]) ; 
		double theta_t = PI * target ;
		tp[0] = TP * cos(theta_0 + theta_t) ; 
		tp[1] = TP * sin(theta_0 + theta_t)  ; 	
		rp[0] += tp[0] - tx.at(N-1) ; 
		rp[1] += tp[1] - ty.at(N-1) ; 
		tx[N-1] = tp[0] ; 
		ty[N-1] = tp[1] ;
		// this changes RP a little bit 
		RP = getRP() ;

		phi.at(N-1) = atan_proper(tp[0],tp[1])  ; 

	}

	savestate() ; 
}

void adjustRP(double target) {
	// @param: target RP/N val (in [0,1] )
	_Nm2 = 1./(N-2) ; 

	double txi = N * _Nm2 *target /  sqrt2 - tp[0]*_Nm2 ;

	rp[0] = 0.0 ; 
	rp[1] = 0.0 ; 
	for(int i = 1 ; i +1 < N ; i++) {

		tx.at(i) = txi ; 
		ty.at(i) = txi ;
		tz.at(i) = sqrt(1 - 2*txi*txi) ; 

		psi.at(i) = tz.at(i) ; 
		if (tx.at(i) != 0 ) phi.at(i) = atan(ty.at(i)/tx.at(i)) ; 
		else phi.at(i) = ophi.at(i) ; 


		rp[0] += txi ; 
		rp[1] += txi ; 
	}

	rp[0] += tp[0] ; 
	rp[1] += tp[1] ; 


	RP = getRP() ; 
	checkNorms(); 

}

void adjustTP(double target) {

	double tp_ip = target/sqrt(2); 
	double t_z =  sqrt(1. - target*target)  ; 
	tp[0] = tp_ip  ; 
	tp[1] = tp_ip  ; 

	rp[0] += (tp[0] - tx[N-1] ) ; 
	rp[1] += (tp[1] - ty[N-1] ) ; 

	tx[N-1] = tp[0] ; 
	ty[N-1] = tp[1] ; 
	tz[N-1] = t_z ; 

	phi.at(N-1) = PI/4. ; 
	psi.at(N-1) = t_z ; 

	TP = getTP() ;
}




// monte carlo move acceptance/rejection criteria 
int mc_step() {

	//double z_prev = getZ() ; 
	savestate() ; 
	double z_curr = getZ() ; 
	if (z_curr > zmax) zmax = z_curr ; 
	double E0 = getE() ; 
	
	int ip  = 1 + rng.randExc() * (N-2) ; 
	int jp =  1 + rng.randExc() * (N-2) ; 
	//cout << ip << " "<< jp << endl ;
	int OK = perturb(ip,jp) ; 

	if(!OK) {
		revert(ip) ; 
		revert(jp) ; 
		return 0 ; 
	}

	double dE = getE() - E0 ; 

	// Metropolis part 
	urn = rng.rand() ; 
	if ( urn > exp(-dE) * opsi.at(jp) / psi.at(jp) ) {
		revert(ip); 
		revert(jp); 
		return 0;
	}

	return 1; 

}

double getBiasedE(int wi ) { 

	return getE() + V_bias(getZ(),wi) ; 
}

void writeZ(int step) { 
	int wi = 0 ; 
	double z_curr = getZ() ; 
	//cout << z_curr << endl ;
	double bin_index = floor( z_curr * nbins) ; 

	zHists[wi][bin_index] += 1 ; 
	totalCounts += 1 ; 

	for(int i = 0 ; i< nMoments; i++ ) {
		zMoments[i] += pow( z_curr, i+1) ; 
	}
}

void write_cosines() {
	for(int j =0; j< N-1; j++) {
		double tcos = innerProduct(tx.at(j),ty.at(j),tz.at(j),tx[j+1],ty[j+1],tz.at(j+1));  
		int bin_index = floor((0.5 + 0.5*tcos )* nbins) ; 
		if (bin_index > 0) {
			cosHist[bin_index] += 1; 
		}
	}
}

void writeZMoments() { 
	int wi = 0 ; 
	fout.open("moments.dat"); 
	for(int i = 0 ; i < nMoments; i++) { 
		double TC = totalCounts ; 
		zMoments[i] /=  TC ; 
		if (TC > 100 ) {
			fout << i+1 ; 
			fout << setw(15) << zMoments[i] ; 
			fout << endl ; 
		}
	}
	fout.close(); 
	fout.clear();
}


void writeZFile(int step) {
	int wi = 0 ; 
	char zString[40];
	sprintf(zString,"%d\t%f\t%f\n",step, getZ() , getE()); 
	fputs(zString,windowFiles[wi]);

}

void writeCoordinates( ) {

	xi = 0.0 ; 
	yi = 0.0 ; 
	zi = 0.0 ; 
	coorFile << N << endl ; 
	coorFile << endl ; 
	for(int i = 0 ; i < N ; i++) {

		xi += tx.at(i) ; 
		yi += ty.at(i) ; 
		zi += tz.at(i) ; 
		coorFile << 1  ;
		coorFile << " " ; 
		coorFile << xi ; 
		coorFile << " " ; 
		coorFile << yi ; 
		coorFile << " " ; 
		coorFile << zi ; 
		coorFile << endl ; 
	}
}


void WriteEventData(int step) {

	writeZ(step); 
	//writeZFile(step); 
	//getCorrelator() ; 
	//writeCoordinates() ; 
}

void writeHistograms(int wi = 0 ) {

	writeZMoments() ;
	double P, binContent;
	//fout.open("cosines.dat"); 

	double TC = totalCounts ; 

	double maxP = 0.0  ;
	for(int i = 0; i < nbins; i++) {
		double binLowEdge = i/(double) nbins ; 
		double binCenter = binLowEdge + 1/(2.*nbins) ; 
		binContent = zHists[wi][i]; 
		P = binContent / TC ; 
		if (P > maxP ) {
			maxP = P ; 
			z_mp = binCenter ; 
		}

		char histVals[25]; 
		if(binContent >100 ) {
			sprintf(histVals,"%f\t%f\n",binCenter, - log(P) ); 
			fputs(histVals,histFiles[0]) ;

		}

	}
}


void writeLogFile() { 

	fout.open("log.dat"); 
	fout << "RP " << setw(15) << RP << endl ; 
	fout << "TP " << setw(15) << TP << endl ; 
	fout << "RPTP " << setw(15) << RPTP << endl ; 
	fout << "zmax " << setw(15) << zmax << endl ; 
	fout << "Zmp " << setw(15) << z_mp << endl; 
	fout.close() ; 
	fout.clear() ; 
}


int cleanup() {
	fclose(zFile); 
	fclose(progressFile);
	//coorFile.close() ; 
	cout << "all files closed " << endl ; 
	return 0 ; 
}

