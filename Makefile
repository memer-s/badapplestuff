all: compile link

compile:
	g++ -c reader.cpp

link: 
	g++ reader.o -o reader