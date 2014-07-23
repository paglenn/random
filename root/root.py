import ROOT

c1 = ROOT.TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )

#
# Create a one dimensional function and draw it
#
fun1 = ROOT.TF1( 'fun1', 'abs(sin(x)/x)', 0, 10 )

c1.SetGridx()
c1.SetGridy()
fun1.Draw()
c1.SaveAs("mylife.png")




#raw_input('Exit: ')
