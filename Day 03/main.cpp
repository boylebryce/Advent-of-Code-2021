#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int boolArrayToInt(bool* input, int columns) {
    int output = 0;
    int exponent = columns - 1;

    for(int i = 0; i < columns; i++) {
        if(input[i]) {
            output += pow(2, exponent);
        }

        exponent--;
    }

    return output;
}

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
    vector<bool*> bitArrays;
    // = new bool*[input.size()];

    // Create arrays of bool
    for (int i = 0; i < input.size(); i++) {
        bitArrays.push_back(new bool[columns]);

        // Initialize bools
        for (int j = 0; j < columns; j++) {
            bitArrays[i][j] = input[i].at(j) == '1' ? true : false;
        }
    }

/* Construct gamma and epsilon bit arrays */
    bool* gamma = new bool[columns];
    bool* epsilon = new bool[columns];

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

        gamma[i] = ones > zeros;
        epsilon[i] = !gamma[i];
    }

/* Convert bit arrays to decimal values */
    int gammaValue = boolArrayToInt(gamma, columns);
    int epsilonValue = boolArrayToInt(epsilon, columns);

/* Part one output */
    cout << gammaValue * epsilonValue << endl;

/* Part two */
    bool includeFlag;

/* Oxygen */
    vector<bool*> oxygenBitArrays = bitArrays;

    // Iterate over columns
    for(int i = 0; i < columns; i++) {
        int ones = 0;
        int zeros = 0;
        vector<int> eraseIndices;

        // Iterate over rows to count 0s and 1s
        for (int j = 0; j < oxygenBitArrays.size(); j++) {
            if(oxygenBitArrays[j][i]) {
                ones++;
            }
            else {
                zeros++;
            }
        }

        includeFlag = ones >= zeros;

        // Get row indices to erase
        for (int j = 0; j < oxygenBitArrays.size(); j++) {
            if(!(oxygenBitArrays[j][i] == includeFlag)) {
                eraseIndices.push_back(j);
            }
        }

        // Erase rows
        for (int j = 0; j < eraseIndices.size(); j++) {
            oxygenBitArrays.erase(oxygenBitArrays.begin() + (eraseIndices[j] - j));
        }
    }

/* CO2 scrubber */
    vector<bool*> scrubberBitArrays = bitArrays;

    // Iterate over columns
    for(int i = 0; i < columns; i++) {
        int ones = 0;
        int zeros = 0;
        vector<int> eraseIndices;

        // Iterate over rows to count 0s and 1s
        for (int j = 0; j < scrubberBitArrays.size(); j++) {
            if(scrubberBitArrays[j][i]) {
                ones++;
            }
            else {
                zeros++;
            }
        }

        includeFlag = ones < zeros;

        // Get row indices to erase
        for (int j = 0; j < scrubberBitArrays.size(); j++) {
            if(!(scrubberBitArrays[j][i] == includeFlag)) {
                eraseIndices.push_back(j);
            }
        }

        // Erase rows
        for (int j = 0; j < eraseIndices.size(); j++) {
            scrubberBitArrays.erase(scrubberBitArrays.begin() + (eraseIndices[j] - j));
        }
    }

    int oxygenValue = boolArrayToInt(oxygenBitArrays[0], columns);
    int scrubberValue = boolArrayToInt(scrubberBitArrays[0], columns);

    cout << "Oxygen generator: " << oxygenValue << endl;
    cout << "CO2 scrubber: " << scrubberValue << endl;
    cout << "Life support rating: " << oxygenValue * scrubberValue << endl;

}