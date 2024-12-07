#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <math.h>
#include <stdbool.h>
#include <time.h>

int main(){
    srand(clock());
    int i, r;
    for(i = 0; i<100; i++){
        r = rand(); 
        printf("%d\n", r);
    }
    

}