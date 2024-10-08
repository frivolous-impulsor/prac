#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>

int numMails = 0;
pthread_mutex_t mutex; //define/create a mutex

void* mailIncreament(){
    for (int i = 0; i < 100000; i++){
        pthread_mutex_lock(&mutex);
        numMails++;
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

int forLoopCreateThread(int size){
    int i;
    pthread_t threads[size];
    pthread_mutex_init(&mutex, NULL);   //initialize mutex lock
    for(i = 0; i< size; i++){
        if(pthread_create(threads+i, NULL, &mailIncreament, NULL)){
            return i;
        }
        printf("thread numebr %d started\n", i);
    }
    for(i = 0; i < size; i++){
        if(pthread_join(threads[i], NULL)){
            return size+1;
        }
        printf("thread numebr %d ended\n", i);
    }
    pthread_mutex_destroy(&mutex);
    printf("number of mail: %d\n", numMails);
    return 0;
}

void* rollDice(){
    int num = rand()%6 + 1;
    int* result = malloc(sizeof(int));
    *result = num;
    printf("address of result: %p\n", result);
    return (void*)result;
}

int returnValOfThread(){
    srand(time(NULL));
    int* res;
    pthread_t t;
    if(pthread_create(&t, NULL, &rollDice, NULL)){
        return 1;
    }
    if(pthread_join(t, (void **)&res)){
        return 2;
    }
    printf("address of res: %p\n", res);

    printf("result is %d\n", *res);
    free(res);

    return 0;
}

int main(int argc, char* argv[]){
    char str[] = "hello";
    printf("%02x\n", str);
    return 0;
}