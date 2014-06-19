// From CERN ROOT Primer 
// Toy Monte Carlo Example 
// Check pull distribution to compare chi2 and binned log-lik methods
//

pull(int n_toys = int(1e5), int n_tot_entries = 100, int nbins = 40, 
		bool do_chi2 = true) {

	TString method_prefix("Log-likelihood") ; 
	if (do_chi2) method_prefix = "#chi^{2}" ;

	//Create histo 
	TH1F* h4 = new TH1F(method_prefix+"h4", method_prefix+"random Gauss", 
			nbins, -4, 4) ;
	h4-> SetMarkerStyle(21); 
	h4 -> SetMarkerSize(0.8); 
	h4 -> SetMarkerColor(kRed); 

	//Histogram for sigma and pull 
	TH1F* sigma = new TH1F(method_prefix+"sigma", 
				method_prefix+"pull from gaus fit", 50, 0.5, 1.5) ;
	TH1F* pull = new TH1F(method_prefix+"pull",method_prefix+"pull from gaus fit",
				50,-4.,4.);

	//Make nice canvases
	TCanvas* c0 = new TCanvas(method_prefix+"Gauss",method_prefix+"Gauss",
				0,0,320,240);
	c0 -> SetGrid() ;

	TCanvas* c1 = new TCanvas(method_prefix+"Result", 
					method_prefix+"Sigma-Distribution",
					0,300,600,400);
	c0->cd();

	float sig, mean; 
	for (int i = 0; i <n_toys; i++ ) {
		//Reset histogram contents 
		h4->Reset();
		
		//Fill histo
		for (int j = 0; i<n_tot_entries; j++ )
			h4->Fill(gRandom->Gaus()) ;
		
		// Perform fit
		if(do_chi2) h4->Fit("gaus","q") ; //Chi2 fit (how?)
		else h4->Fit("gaus", "lq") // Likelihood fit 
		
		//some control output on the way (?) 
		if (!(i%100)){
			h4->Draw("ep");
			c0->Update();
		}

		// Get sigma from fit 
		TF1 *fit = h4-> GetFunction("gaus");
		mean = fit -> GetParameter(1); 
		sig = fit-> GetParameter(2);
		sigma -> Fill(sig);
		pull -> Fill(mean/sig * sqrt(n_tot_entries));

	} // end of toy MC loop 
	// print result 
	c1 -> cd();
	pull->Draw();

}

void macro9() {
	int n_toys = int(1e3); 
	int n_tot_entries = 100; 
	int n_bins = 40;  
	cout << "Performing pull experiment with chi2 \n";
	pull(n_toys, n_tot_entries, n_bins, true );
	cout << " Performing Pull Experiment with Log Likelihood \n" ;
	pull(n_toys, n_tot_entries, n_bins, false);
}

