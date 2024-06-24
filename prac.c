#include <stdio.h>
#include <string.h>

typedef char username[25];

typedef struct 
{
    /* data */
    username name;
    int userId;
}User;

typedef struct
{
    /* data */
    char name[25];
    char major[25];
}Student;



void printArray(int arr[], int len){
    for(int i = 0; i < len; i++){
        printf("%d\n",arr[i]);
    }
}

void bubbleSort(int array[], int len){

    for(int i = 0; i < len-2; i++){
        for(int j=0; j < len-1; j++){
            if(array[j] > array[j+1]){
                int temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
    printArray(array, len);
}

int main(){
    Student s1 = {"batman", "material engineering"};
    Student s2 = {"ironman", "mechanical engineering"};
    Student s3 = {"hawk", "physics"};

    Student students[3] = {s1, s2, s3};

    for(int i = 0; i < sizeof(students)/sizeof(students[0]); i++ ){
        printf("%-18s", students[i].name);
        printf("%-18s\n", students[i].major);
    }
    
    return 0;
}
 