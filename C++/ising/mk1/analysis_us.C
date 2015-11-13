{
	const int numWindows = 10; 
	TFile * data = new TFile("data_us.root"); 
	TH1 * hists[numWindows] ; 
	hists[0] = magHist_0 ; 
	hists[1] = magHist_1 ; 
	hists[2] = magHist_2 ; 
	hists[3] = magHist_3 ; 
	hists[4] = magHist_4 ; 
	hists[5] = magHist_5 ; 
	hists[6] = magHist_6 ; 
	hists[7] = magHist_7 ; 
	hists[8] = magHist_8 ; 
	hists[9] = magHist_9 ; 
	
	for(int i = 0 ; i < numWindows; i++) {
		hists[i]->Scale(1./hists[i]->Integral("width")) ; 
	}
	
	//TCanvas * canvas = new TCanvas("combined", "combined"); 
	TProfile * final; 
	for(int i = 0 ; i < numWindows; i++) {
		
		//if (i == 0) hists[i]->Draw("C"); 
		//else hists[i]->Draw("same C"); 
	}
	/*

	for (int i = 0; i + 1 <  numWindows; i++) {
		double upper = hists[i]->GetBinContent(hists[i]->GetNbinsX()) ; 
		if (upper == 0) cout << "problem!" << endl; 
		double mod = hists[i+1]->GetBinContent(1)/hists[i]->GetBinContent(hists[i]->GetNbinsX());
		hists[i]->Scale(mod); 
	}
	TCanvas * canvas = new TCanvas("combined", "combined"); 
	for(int i = 0 ; i < numWindows; i++) {

		hists[i]->Draw("same C"); 
	}
	*/



}
