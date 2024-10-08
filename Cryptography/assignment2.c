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
    return 0;
}


int padding(char *str, int size){
    int l = size * 8;   //length of original str in bits
    long long length64 = l;

    int k = 512 - ((l + 64 + 1) % 512); //!!!NOT CORRECT LOGIC
    printf("k: %d\n",k);

    int totalSizeBit = l + 64 + 1 + k;  //should be multiple of 512
    printf("total: %d\n",totalSizeBit);
    char* res = malloc(sizeof(char) * (totalSizeBit/8));
    int i, j;
    for(i = 0; i<size; i++){
        res[i] = str[i];
    }
    res[size] = 0x80;    //append 1
    for(j = 8; j >=1; j--){     //append the length of original str as a 8-byte integer
        res[totalSizeBit/8 - j] = (length64 >> (j-1)*8) & 0xff;
    }
    //printStrInBinary(res, totalSizeBit/512);
    printStrInBinary(res, totalSizeBit/8);

    free(res);
    return 0;
}

int main(int argc, char* argv[]){
    char test[] = "Quel res so los de combrestro, los por cua, de de de vella los, de de nombrincir dejanchescrisadalpicón de para. Pernesay algun laba quijad de lastrecinción adompla asobra quenía ollanzas sábas fientes de tos de vierenjetuflomigo a questo mo, que día la entufla no de los tilesalgo hayo de secina porí dos panza. Tendador quellese veina el ro, nompordadifer dor. Quijadaresta, añados fincludor que naredos des de comillantre no pas de Quijasta, y una. Fringo hidartas de honra quelo años, nuesempordada,";
    int len =strlen(test);
    printf("%d\n", len);
    padding(test, len);
    return 0;
}