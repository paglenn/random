#Convert from Fahrenheit degrees to Kelvin

F=raw_input("Input a value for Fahrenheit Degrees: ")
C=5*(float(F)-32)/9
Kelvin=C+273.16

print str(F)+' is ' +str(Kelvin)+ ' Kelvin. You can check this because it is '+str(C) + \
      ' degrees Celsius.'
      
