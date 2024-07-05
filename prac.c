#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
void arrayInHex(int *arr, int size){
    for(int i = 0; i < size; i++){
        printf("%08x\n", arr[i]);
    }
}

void bytePrint(void *arr, int size){
    for(int i = 0; i<size; i++){
        printf("%02x  ", ((char*)arr)[i]);
    }
}



int main() {
    int a = 71;
    printf("%c\n", a);
    
}