#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <windows.h>

using namespace std;

int main() {
    string line;
    ifstream myfile;
    int linenumber = 0;
    myfile.open("script.manus");
    if (myfile.is_open())
    {
        while ( getline(myfile,line) )
        {
            linenumber = linenumber + 1;
            if (linenumber % 72 == 0)
            {
                Sleep(80);
            }
            
            cout << line << '\n';
        }

        myfile.close();
    }
    
}