#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){

    int age = 20;

    int *pAge = &age;

    
    printf("age value is: %d\n", age);
    printf("value at address is : %d\n", *pAge);
    printf("age address is: %p\n", &age);
    printf("address of age is: %p\n", pAge);
    
    return 0;
}
 