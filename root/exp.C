{
	TF1* efunc = new TF1("efunc","exp([0]+[1]*x)",0.,5.) ;
	efunc -> SetParameter(1,-1);
	efunc -> Draw();
}


