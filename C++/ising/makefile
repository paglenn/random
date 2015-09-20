basic: basic.cpp Lattice.h methods.h  
	g++ -O3 basic.cpp `root-config --cflags --libs` -o basic
temp: temp.cpp Lattice.h methods.h  
	g++ -O3 temp.cpp `root-config --cflags --libs` -o temp
umbrella: umbrella.cpp Lattice.h methods.h 
	g++ -O3 umbrella.cpp `root-config --cflags --libs` -o umbrella
clean: 
	rm basic &> /dev/null 
	rm temp &> /dev/null
	make 
