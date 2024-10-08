#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int printStrInBinary(char *str, int size){
    int i,j;
    for(i = 0; i< size; i++){
        char byte = str[i];
        for(j = 7; j >=0; j--){
            char bit = (byte >> j) & 1;
            printf("%hhd", bit);
        }
        printf(" ");
    }
}

int padding(char *str, int size, char *result){
    int l = size * 8;   //length of original str in bits
    int k = (l + 64 + 1) % 512;
    int totalSizeBit = l + 64 + 1 + k;  //should be multiple of 512
    char* res = malloc(sizeof(char) * (totalSizeBit/512));
    int numBitAppend = totalSizeBit - l;
    char* 
    
    printf("%d", k);
    free(res);
    return 0;
}

int main(int argc, char* argv[]){
    char str[] = "abc";
    int len = strlen(str);
    printStrInBinary(str, len);

    return 0;
}