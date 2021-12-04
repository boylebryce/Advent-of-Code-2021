#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main() {
/* Parse input file to array of strings */
    ifstream inputFile;
    inputFile.open("input.txt");

    vector<string> input;
    string line;

    while(getline(inputFile, line)) {
        input.push_back(line);
    }

    inputFile.close();

/* Cast input strings to 2D array of bools */
    int columns = input[0].length();
    
    // Array of pointers to arrays of bool to create dynamic 2D array
    bool** bitArrays = new bool*[input.size()];

    // Create arrays of bool
    for (int i = 0; i < input.size(); i++) {
        bitArrays[i] = new bool[columns];

        // Initialize bools
        for (int j = 0; j < columns; j++) {
            bitArrays[i][j] = input[i].at(j) == '1' ? true : false;
        }
    }

/* Construct gamma and epsilon bit arrays */
    vector<bool> gamma;
    vector<bool> epsilon;

    // Iterate over columns
    for(int i = 0; i < columns; i++) {
        int ones = 0;
        int zeros = 0;

        // Iterate over rows
        for (int j = 0; j < input.size(); j++) {
            if(bitArrays[j][i]) {
                ones++;
            }
            else {
                zeros++;
            }
        }

        gamma.push_back(ones > zeros);
        epsilon.push_back(!gamma.back());
    }

/* Convert bit arrays to decimal values */
    int gammaValue = 0;
    int epsilonValue = 0;
    int exponent = columns - 1;

    for(int i = 0; i < columns; i++) {
        if(gamma[i]) {
            gammaValue += pow(2, exponent);
        }

        if(epsilon[i]) {
            epsilonValue += pow(2, exponent);
        }

        exponent--;
    }

/* Output */
    cout << gammaValue * epsilonValue << endl;
}