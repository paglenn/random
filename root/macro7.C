void macro7(){
	gStyle->SetPalette(53);
	gStyle->SetOptStat(0);
	gStyle->SetOptTitle(0);

	TH2F bidi_h("bidi_h","2D Histo; Gaussian Vals; Exp.Vals", 30, -5, 5, 30, 0, 10);
	
	TRandom3 rgen; 
	for ( int i=0; i<500000; i++) {
		bidi_h.Fill(rgen.Gaus(0,2),10-rgen.Exp(4),.1);
	}
	TCanvas* c1 = new TCanvas("Canvas", "Canvas", 800, 800);
	//Divide into a 2x2 
	c1->Divide(2,2);
	c1->cd(1); bidi_h.DrawClone("Cont1");
	c1->cd(2); bidi_h.DrawClone("Colz");
	c1->cd(3); bidi_h.DrawClone("lego2");
	c1->cd(4); bidi_h.DrawClone("surf3");
	
	/*
	//Profiles and projections 
	TCanvas* c2 = new TCanvas("Canvas2", "Canvas2", 800,800);
	c2 -> Divide(2,2);
	c2 -> cd(1); bidi_h.ProjectionX() -> DrawClone() ;
	c2 -> cd(2); bidi_h.ProjectionY() -> DrawClone() ;
	c2 -> cd(3); bidi_h.ProfileX() -> DrawClone() ;
	c2 -> cd(4); bidi_h.ProfileY() -> DrawClone() ;
	*/
}
	
	
