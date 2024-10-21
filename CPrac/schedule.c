#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <sys/time.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <signal.h>

typedef struct {
    int *elements;   // Array to store elements
    int *priority;   // Array to store priorities
    int *index;      // Array to store index of each element in the heap
    int capacity;    // Maximum number of elements
    int size;        // Current number of elements
} IndexedPriorityQueue;

// Function to create an indexed priority queue
IndexedPriorityQueue* createIndexedPriorityQueue(int capacity) {
    IndexedPriorityQueue* pq = (IndexedPriorityQueue*)malloc(sizeof(IndexedPriorityQueue));
    pq->capacity = capacity;
    pq->size = 0;
    pq->elements = (int*)malloc(capacity * sizeof(int));
    pq->priority = (int*)malloc(capacity * sizeof(int));
    pq->index = (int*)malloc(capacity * sizeof(int));
    
    for (int i = 0; i < capacity; i++) {
        pq->index[i] = -1; // Initialize indices to -1 (not in queue)
    }
    
    return pq;
}

// Function to swap two elements
void swap(IndexedPriorityQueue *pq, int a, int b) {
    int temp = pq->elements[a];
    pq->elements[a] = pq->elements[b];
    pq->elements[b] = temp;

    temp = pq->priority[a];
    pq->priority[a] = pq->priority[b];
    pq->priority[b] = temp;

    pq->index[pq->elements[a]] = a;
    pq->index[pq->elements[b]] = b;
}

// Function to heapify down
void heapifyDown(IndexedPriorityQueue *pq, int idx) {
    int smallest = idx;
    int left = 2 * idx + 1;
    int right = 2 * idx + 2;

    if (left < pq->size && pq->priority[pq->elements[left]] < pq->priority[pq->elements[smallest]]) {
        smallest = left;
    }
    if (right < pq->size && pq->priority[pq->elements[right]] < pq->priority[pq->elements[smallest]]) {
        smallest = right;
    }
    if (smallest != idx) {
        swap(pq, idx, smallest);
        heapifyDown(pq, smallest);
    }
}

// Function to heapify up
void heapifyUp(IndexedPriorityQueue *pq, int idx) {
    while (idx && pq->priority[pq->elements[idx]] < pq->priority[pq->elements[(idx - 1) / 2]]) {
        swap(pq, idx, (idx - 1) / 2);
        idx = (idx - 1) / 2;
    }
}

// Function to insert an element
void insert(IndexedPriorityQueue *pq, int element, int priority) {
    if (pq->size >= pq->capacity) {
        printf("Queue is full\n");
        return;
    }
    pq->elements[pq->size] = element;
    pq->priority[element] = priority;
    pq->index[element] = pq->size;
    pq->size++;
    heapifyUp(pq, pq->size - 1);
}

// Function to extract the minimum element
int extractMin(IndexedPriorityQueue *pq) {
    if (pq->size == 0) {
        printf("Queue is empty\n");
        return -1;
    }
    int minElement = pq->elements[0];
    pq->elements[0] = pq->elements[pq->size - 1];
    pq->index[pq->elements[0]] = 0;
    pq->size--;
    heapifyDown(pq, 0);
    return minElement;
}

// Function to decrease the priority of an element
void decreasePriority(IndexedPriorityQueue *pq, int element, int newPriority) {
    if (pq->index[element] == -1) {
        printf("Element not found\n");
        return;
    }
    if (newPriority > pq->priority[element]) {
        printf("New priority is greater than current priority\n");
        return;
    }
    pq->priority[element] = newPriority;
    heapifyUp(pq, pq->index[element]);
}

// Function to free the indexed priority queue
void freeIndexedPriorityQueue(IndexedPriorityQueue *pq) {
    free(pq->elements);
    free(pq->priority);
    free(pq->index);
    free(pq);
}


struct timeval t1;

typedef struct
{
    /* data */
    pid_t pid;
    int deadline;
    int capacity;
} Task;

int getRandomInt(int max, int* pResult){
    gettimeofday(&t1, NULL);
    srand(t1.tv_usec * t1.tv_sec);
    int num = rand();
    *pResult = num % (max+1);
    return 0;
}

int createRandomProcess(Task* t){
    pid_t pid = fork();
    if (pid == -1){
        printf("fork failed\n");
        return 1;
    }
    if (pid != 0){
        t->pid = pid;
        int deadline;
        getRandomInt(20, &deadline); //each 
        t->deadline = deadline;
        t->capacity = 2;
        wait(NULL);
    } 
    else{
        exit(0);
    }
    return 0;
}



int main() {
    IndexedPriorityQueue readyQueue = *createIndexedPriorityQueue(30);
    pid_t pid = fork();
    if(pid == -1){
        printf("fork failed\n");
        return 1;
    }
    if(pid == 0){
        //chile process for selecting and executing tasks
        while(true){
            if(readyQueue.size > 0){
                printf("REACHED EXECUTION PART\n");

                int currentTaskId = extractMin(&readyQueue);
                sleep(2); //assuming each task requires 2 seconds of CPU execution time
                kill(currentTaskId, SIGKILL);
                printf("task %d finished execution\n", currentTaskId);
                for(int i = 0; i < readyQueue.size ; i++){
                    if (readyQueue.priority[i] <= 2){
                        printf("task %d failed\n", readyQueue.elements[i]);
                    }else{
                        readyQueue.priority[i] -=2;
                    }
                    ; //decrease the deadline of all remaining tasks by 2 sec
                }
            }else{
                sleep(2);
            }
            
        }


        
    }else{
        //parent process for generating tasks sparadically
        while(true){
            Task t; //initiallize a task of {pid, deadline, capacity}
            createRandomProcess(&t);
            printf("task %d of dealine %d is created\n", t.pid, t.deadline);
            insert(&readyQueue, t.pid, t.deadline);
            int sleepTime;
            getRandomInt(3, &sleepTime);
            sleep(sleepTime); //enqueue new task to ready queue sparadically
        }
    }
    
    
    return 0;
}