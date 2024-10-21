#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>
#include <string.h>
#include <semaphore.h>


#define SHELF_MAX 10
#define THREAD_NUM 2
int shelf[SHELF_MAX];
int pointer;
pthread_mutex_t shelfMutex;
sem_t productSema;
sem_t spotSema;
pthread_t th[THREAD_NUM];

void* consume(void* arg){
    int consumed;
    while(1){
        sem_wait(&productSema);
        //take from shelf
        pthread_mutex_lock(&shelfMutex);
        consumed = shelf[pointer-1];
        pointer--;
        pthread_mutex_unlock(&shelfMutex);
        sem_post(&spotSema);
        //consume
        printf("Consumed %d\n", consumed);
        sleep(1);
        
    }
    return NULL;
}

void* produce(void* arg){
    while(1){
        //produce
        int produced = rand()%100+1;
        sleep(1);
        //put on shelf
        sem_wait(&spotSema);
        pthread_mutex_lock(&shelfMutex);
        shelf[pointer] = produced;
        pointer++;
        pthread_mutex_unlock(&shelfMutex);
        sem_post(&productSema);
        
    }
    return NULL;
}

int main(){
    srand(time(NULL));
    int i;
    pointer = 0;
    pthread_mutex_init(&shelfMutex, NULL);
    sem_init(&productSema, 0, 0);
    sem_init(&spotSema, 0, SHELF_MAX);
    for(i = 0; i<THREAD_NUM; i++){
        if(i){
            if(pthread_create(&th[i], NULL, &consume, NULL)){
                return i;
            }
        } else{
            if(pthread_create(&th[i], NULL, &produce, NULL)){
                return i;
            }
        }

    }

    for(i = 0; i<THREAD_NUM; i++){
        if(pthread_join(th[i], NULL)){
            return i + THREAD_NUM;
        }
    }
    pthread_mutex_destroy(&shelfMutex);
    sem_destroy(&productSema);
    sem_destroy(&spotSema);
    return 0;
}