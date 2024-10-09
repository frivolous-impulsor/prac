#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>


int printStrInBinary(char *str, int size);
int padding(char *str, int size, char *output);

int rightRotate(int num, int iterations);


int messageSchedule(char* padded, int len);

int Ch(int x, int y, int z);
int Ma(int x, int y, int z){
    return (x & y) ^ (x & ~z) ^ (y & z);
}
int CAPsig0(int x){
    int result;
    return 0;
}



int main(int argc, char* argv[]){


    int h0, h1, h2, h3, h4, h5, h6, h7;
    h0 = 0x6a09e667;
    h1 = 0xbb67ae85;
    h2 = 0x3c6ef372;
    h3 = 0xa54ff53a;
    h4 = 0x510e527f;
    h5 = 0x9b05688c;
    h6 = 0x1f83d9ab;
    h7 = 0x5be0cd19;
    int a = 0x94;
    printf("before %02x\n", a);

    a = rightRotate(a, 6);
    printf("after %02x\n", a);

    return 0;
}

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
    return 0;
}

int padding(char *str, int size, char *output){
    int l = size * 8;   //length of original str in bits
    long long length64 = l;

    int k = 512 - ((l + 64 + 1) % 512); //!!!NOT CORRECT LOGIC

    int totalSizeBit = l + 64 + 1 + k;  //should be multiple of 512
    char *res = calloc(totalSizeBit/8, sizeof(char));
    int i, j, m;
    for(i = 0; i<size; i++){
        res[i] = str[i];
    }
    res[size] = 0x80;    //append 1
    for(j = 8; j >=1; j--){     //append the length of original str as a 8-byte integer
        res[totalSizeBit/8 - j] = (length64 >> (j-1)*8) & 0xff;
    }
    printStrInBinary(res, totalSizeBit/8);
    printf("\nseparate: \n");
    for(m = 0; m < totalSizeBit/8; m++){
        output[m] = res[m];
    }
    free(res);
    return totalSizeBit;
}

int rightRotate(int num, int iterations){    //rotate
    int i, shadow, lsDigit;
    shadow = 1;
    for(i = 0; i< iterations; i++){
        lsDigit = shadow & num;
        num = num >> 1;
        if (lsDigit){
            num = num | 0x80000000;
        } else{
            num = num & 0x7fffffff;
        }
    }
    return num;
}

int Ch(int x, int y, int z){
    return (x & y) ^ (x & z);
}
