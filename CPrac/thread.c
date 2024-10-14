#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>
#include <string.h>

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

int returnValofThreads(){
    srand(time(NULL));
    int i;
    int* res[8];
    pthread_t threads[8];
    for(i = 0; i< 8; i++){
        if(pthread_create(&threads[i], NULL, &rollDice, NULL)){
            return i;
        }
        sleep(1);
    }
    for(i = 0; i<8; i++){
        if(pthread_join(threads[i], (void **)&res[i])){
            return i + 8;
        }
    }

    for(i = 0; i<8; i++){
        printf("result of roll %d: %d\n", i, *res[i]);
        free(res[i]);
    }

    return 0;
}

void* printPrime(void* arg){
    printf("%d ", *(int*)arg);
    return NULL;
}
int primes[] = {2,3,5,7,11,13,17,19,23,29};

int passArg(){
    pthread_t threads[2]; 
    int i;
    for(i = 0; i< 10; i++){
        if(pthread_create(&threads[i], NULL, &printPrime, primes + i)){
            return i;
        }

    }
    for(i = 0; i<10; i++){
        if(pthread_join(threads[i], NULL)){
            return i + 10;
        }
    }
    return 0;
}

void* sumPrime(void* start){
    int* result = malloc(sizeof(int));
    *result = 0;
    for(int i = 0; i<5; i++){
        *result = *result + *((int*)start + i);
    }
    return (void*)result;
}

int sumPrimesThreads(){
    int* pTemp;
    int result = 0;
    int numThread = 2;
    pthread_t threads[numThread];
    int i;
    int mid = sizeof(primes)/sizeof(int) /numThread;
    for(i = 0; i<numThread; i++){
        if(pthread_create(&threads[i], NULL, &sumPrime, primes+i*mid)){
            return i;
        }
    }
    for(i = 0; i<numThread; i++){
        if(pthread_join(threads[i], (void**)&pTemp)){
            return numThread + i;
        }
        result = result + *pTemp;
        free(pTemp);
    }
    printf("sum of first 10 primes is %d\n", result);
    return 0;
}


pthread_mutex_t gasMutex;
pthread_cond_t condGas;
int feulValue = 0;

void* feuling(void* arg){
    for(int i = 0; i<5; i++){
        pthread_mutex_lock(&gasMutex);
        feulValue += 60;
        printf("feul added, current feul at %d\n", feulValue);

        pthread_mutex_unlock(&gasMutex);
        pthread_cond_broadcast(&condGas);

        sleep(1);


    }
    
    return NULL;
}

void* gettingGas(void* arg){
    pthread_mutex_lock(&gasMutex);
    while(feulValue < 40){
        printf("insufficient feul... Current feul at %d\n", feulValue);
        pthread_cond_wait(&condGas, &gasMutex);
        //releasing the mutex; wait until a signal sends in
        //when a signal sends in; reacquire the mutex
    }
    feulValue -= 40;
    printf("got feul, current feul at %d\n", feulValue);
    pthread_mutex_unlock(&gasMutex);
    return NULL;
}


int gasStation(){
    int i;
    pthread_mutex_init(&gasMutex, NULL);
    pthread_cond_init(&condGas, NULL);
    //gas station has 2 parties, feuler that fills the tank and the car that drains the tank

    //thread 0 being feuler and 1 being car
    pthread_t threads[5];

    
    
    if(pthread_create(&threads[0], NULL, &feuling, NULL)){
        return 1;
    }
    for(i = 1; i< 5; i++){
        if(pthread_create(&threads[i], NULL, &gettingGas, NULL)){
        return i;
        }
    }
    

    for(i = 0; i<5; i++){
        if(pthread_join(threads[0], NULL)){
            return i + 5;
        }

    }

    pthread_mutex_destroy(&gasMutex);
    pthread_cond_destroy(&condGas);
    return 0;
}

pthread_mutex_t stoveMs[4];
int stoves[] = {100, 100, 100, 100};
void* cook(){
    int stoveI = 0;
    int feulNeeded = (rand() % 20) + 10;
    while(1){
        if(feulNeeded <= stoves[stoveI] && pthread_mutex_trylock(&stoveMs[stoveI]) == 0){
            //successful
            stoves[stoveI] -= feulNeeded;
            sleep(1);
            printf("chef done, used %d feul at stove %d\n", feulNeeded, stoveI);
            pthread_mutex_unlock(&stoveMs[stoveI]);
            return NULL;
        }else{
            stoveI = (stoveI + 1) % 4;
        }
    }

    return NULL;
}
//10 chefs cook on 4 stoves, each has gas 100. Each chef cooks once and consume 10-30.
int chefCooking(){
    int i;
    int numChef = 10;
    pthread_t threads[numChef];
    for(i = 0; i < 4; i++){
        pthread_mutex_init(&stoveMs[i], NULL);
    }
    srand(time(NULL));

    for(i = 0; i<numChef; i++){
        if(pthread_create(&threads[i], NULL, &cook, NULL)){
            return i;
        }
    }

    for(i = 0; i<numChef; i++){
        if(pthread_join(threads[i], NULL)){
            return numChef + i;
        }
    }

    for(i = 0; i < 4; i++){
        pthread_mutex_destroy(&stoveMs[i]);
    }
    return 0;
}

int main(int argc, char* argv[]){
    chefCooking();
    return 0;
}