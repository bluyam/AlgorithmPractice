// Kyle Wilson
// CodeEval Challenge 1
// Self Describing Numbers : Easy Difficulty
// 12-19-14

#include <iostream> //needed for I/O
#include <fstream>  //needed for file operations
#include <algorithm> //needed for count
using namespace std; //prevents us from having to use std::x for standard library members

int main(int argc, char *argv[]) {
    string current=""; //current line
    ifstream input(argv[1]); //input file name format for CodeEval
    if(!input) { //file name error checking
        cout << "Invalid input file name. Please run the program once more and try again.\n";
        exit(1);
    }
    while(!input.eof()) {
            getline(input,current); //get current number from input file
            if(current.length()>10) { //make sure that the number is less than 11 digits long; otherwise it cannot be self describing.
                cout << "One or more of these numbers cannot be self describing because it is longer than 10 digits.";
                exit(1);
            }
            bool isSDN=true; //assume the number is self describing
            for (int i=0; i<current.length(); i++) { //go through every digit in current number
                char digit = (char)(((int)'0')+i); //convert positon to char from int
                int numCount = count(current.begin(),current.end(),digit); //use std::count to count occurences of digit
                if (current.at(i) != (char)(((int)'0')+numCount)) //if the condition of SDNs are not met for the current digit, it is not an SDN.
                   isSDN=false;
            }
            if(isSDN) cout << "1\n"; 
            else cout << "0\n";
    }
    return 0;
}