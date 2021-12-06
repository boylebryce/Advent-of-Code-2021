#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

const int BOARD_DIM = 5;

class BingoBoard {
private:
    int board[BOARD_DIM][BOARD_DIM];
    bool isBoardSet = false;
    bool isBingoFound = false;
    vector<int> drawnNumbers;
    int winningNums[BOARD_DIM];

    // If draw is found in board, set coordinates in x and y
    void getDrawCoords(int &x, int &y, int draw) {
        if(!isBoardSet) return;

        for(int i = 0; i < BOARD_DIM; i++) {
            for(int j = 0; j < BOARD_DIM; j++) {
                if(board[i][j] == draw) {
                    x = j;
                    y = i;
                    return;
                }
            }
        }

        x = -1;
        y = -1;
        return;
    };

public:
    void setBoard(int** numbers) {
        for(int i = 0; i < BOARD_DIM; i++) {
            for(int j = 0; j < BOARD_DIM; j++) {
                board[i][j] = numbers[i][j];
            }
        }

        isBoardSet = true;
    };

    BingoBoard() {

    };

    BingoBoard(int** numbers) {
        setBoard(numbers);
    };

    // TODO
    bool isBingo(int* numbers, int size, int draw) {
        if(!isBoardSet) return false;
        if(size < BOARD_DIM) return false;

    };
};

int main() {
    ifstream inputFile;
    inputFile.open("testboards.txt");

    vector<BingoBoard> boards;
    BingoBoard* board = new BingoBoard();
    int boardLines[BOARD_DIM][BOARD_DIM];
    string line;
    int boardNum = 0;
    int rowNum = 0;

    while(getline(inputFile, line)) {
        if(line == "") {

        }
        else {
            
        }
    }
}