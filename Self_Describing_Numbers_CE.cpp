#include <iostream> //needed for I/O
#include <fstream>  //needed for file operations
#include <algorithm>
using namespace std; //prevents us from having to use std::x for standard library members

int main() {
    string current="";
    string ifilename;
    cout << "Enter the name of your input file: ";
    cin >> ifilename;
    ifstream input(ifilename);
    if(!input) {
        cout << "Invalid input file name. Please run the program once more and try again.\n";
        exit(1);
    }
    while(!input.eof()) {
            getline(input,current);
            if(current.length()>10) {
                cout << "One or more of these numbers cannot be self describing because it is longer than 10 digits.";
                exit(1);
            }
            for (int i=0; i<current.length(); i++) {
                if (current.at(i) == count(current.begin(),current.end(),(char)(((int)'0')+i)))
                    cout << "1\n";
                else 
                    cout << "0\n";
            }
    }
}