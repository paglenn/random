{
	TF1* efunc = new TF1("efunc","exp([0]+[1]*x)",0.,5.) ;
	efunc -> SetParameter(1,-1);
	efunc -> Draw();

	TH1F* h= new TH1F("h", "example histogram", 100, 0., 5.);
	for (int i=0; i< 1000; i++) h->Fill(efunc->GetRandom()) ;

	h->DrawNormalized();
}


