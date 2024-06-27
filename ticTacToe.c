#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <string.h>
char board[9];
const char PLYER = 'X';
const char CMPTR = 'O';
const char EMPTY = ' ';

void resetBoard(){
    for(int i = 0; i < 9; i++){
        board[i] = EMPTY;
    }
}

void printBoard(){
    for(int i = 0; i < 3; i++){
        int baseI = i*3;
        printf(" %c | %c | %c\n", board[baseI], board[baseI+1], board[baseI+2]);
        if(i < 2){
            printf("---|---|---\n");
        }
    }
}

bool spotEmpty(int row, int col){
    if(row < 0 || row > 2 || col < 0 || col > 2){
        return 1;
    }
    int insertI = row*3 + col;
    char value = board[insertI];
    return value == EMPTY;
}

int move(bool isPlayer, int row, int col){
    int insertI = row*3 + col;
    board[insertI] = (isPlayer) ? 'X' : 'O';
    return 0;
}

bool isBoardFull(){
    for(int i = 0; i < 9; i++){
        char value = board[i];
        if(value == EMPTY){
            return false;
        }
    }
    return true;
}

bool validCoordinate(int row, int col){
    return !(row < 0 || row > 2 || col < 0 || col > 2);
}

bool hasWinner(){
    int centerI = 4;
    char centerValue = board[centerI];
    bool alignCrossCenter = false;
    if(centerValue != EMPTY){
        alignCrossCenter = (board[centerI-3] == board[centerI+3] && centerValue == board[centerI-3]) || (board[centerI-1] == board[centerI+1] && centerValue == board[centerI-1]) || (board[0] == board[8] && centerValue == board[0]) || (board[2] == board[6] && centerValue == board[2]);

    }

    char topLeftValue = board[0];
    char bottomRightValue = board[8];
    bool alignEdges = false;
    if(topLeftValue != EMPTY){
        alignEdges = (board[1] == board[2] && board[1] == topLeftValue) || (board[3] == board[6] && board[3] == topLeftValue);
    }
    if(bottomRightValue != EMPTY){
        alignEdges = alignEdges || (board[6] == board[7] && board[7] == bottomRightValue) || (board[5] == board[2] && board[2] == bottomRightValue);
    }
    return alignCrossCenter || alignEdges;
}

void decode(int *coordinate, int keyPadNum){
    switch (keyPadNum)
    {
    case 1:
        /* code */
        coordinate[0] = 2;
        coordinate[1] = 0;
        break;
    case 2:
        coordinate[0] = 2;
        coordinate[1] = 1;
        break;
    case 3:
        coordinate[0] = 2;
        coordinate[1] = 2;
        break;
    case 4:
        coordinate[0] = 1;
        coordinate[1] = 0;
        break;
    case 5:
        coordinate[0] = 1;
        coordinate[1] = 1;
        break;
    case 6:
        coordinate[0] = 1;
        coordinate[1] = 2;
        break;
    case 7:
        coordinate[0] = 0;
        coordinate[1] = 0;
        break;
    case 8:
        coordinate[0] = 0;
        coordinate[1] = 1;
        break;
    case 9:
        coordinate[0] = 0;
        coordinate[1] = 2;
        break;
    
    default:
        printf("invalid key strok!");
        break;
    }
}

int main(){
    
    resetBoard();
    
    printBoard();
    
    bool isPlayer = true;
    while(!isBoardFull()){
        
        int inputKey;
        char player = (isPlayer) ? 'X' : 'O';
        printf("You are %c\n", player);
        printf("where to land: ");
        scanf("%d", &inputKey);
        int coordinate[2] = {0};
        decode(coordinate, inputKey);
        int row = coordinate[0];
        int col = coordinate[1];


        if(validCoordinate(row, col) && spotEmpty(row, col)){
            move(isPlayer, row, col);
        } else {
            printf("\ninvalid coordinate!\n");
            printBoard();
            continue;
        }
        printBoard();
        if(hasWinner()){
            printf("We have a winner!!! Winner is: %c", player);
            return 0;
        }
        isPlayer = !isPlayer;

    }
    printf("It's A Draaaaw!!!");
    return 1;
}