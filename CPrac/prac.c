#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <errno.h>
#include <fcntl.h>
#include <signal.h>
#include <pthread.h>



int pipePrac(){
    int fd[2];  //read from fd[0] and write from fd[1]
    if (pipe(fd) == -1){    
        printf("piping unsucessful\n");
        return 1;
    }
    int pid = fork();
    if (pid == -1){
        printf("forking unsucessful\n");
        return 2;
    }
    if (pid == 0){  //child process to send a user input to parent process
        close(fd[0]);
        int num;
        printf("input a number: ");
        scanf("%d", &num);
        if (write(fd[1], &num, sizeof(int)) == -1){
            printf("writing unsucessful\n");
            return 4;
        }
        close(fd[1]);
        printf("child process finished writing\n");
    }else {
        close(fd[1]);
        wait(NULL);
        int receive;
        if (read(fd[0], &receive, sizeof(int)) == -1){
            printf("reading unsucessful\n");
            return 3;
        }
        printf("at parent process, received number %d\n", receive);
        close(fd[0]);
        printf("comm completed\n");

    }
    return 0;
}

int sumWith2Processes(int array[], size_t size, int* pSum){
    int len = size;
    int firstEnd = len/2;

    int fd[2];
    if (pipe(fd) == -1){
        printf("pipe failure\n");
        return 2;
    }

    int pid = fork();
    if(pid == -1){
        printf("fork failure");
        return 1;
    } else if(pid == 0){
        close(fd[0]);
        int firstHalf = 0;
        for(int i = 0; i < firstEnd; i++){
            firstHalf = array[i] + firstHalf;
        }
        if (write(fd[1], &firstHalf, sizeof(int)) == -1){
            printf("write failure\n");
            return 3;
        }
        close(fd[1]);
        exit(0);

    } else {
        wait(NULL);
        close(fd[1]);
        int secondHalf = 0;
        for(int j = firstEnd; j < len; j++){
            secondHalf = array[j] + secondHalf;
        }
        int firstHalf;
        if (read(fd[0], &firstHalf, sizeof(int)) == -1){
            printf("read failure\n");
            return 4;
        }
        *pSum = firstHalf + secondHalf;

    }
    return 0;
}

int fifo(){     //parent process will display any input received from child process through fifo
    if (mkfifo("myfifo", 0777) == -1 && errno != EEXIST){
        printf("make fifo failed\n");
        return 1;
    }
    int pid = fork();
    if(pid == 0){
        int fd = open("myfifo", O_WRONLY);
        
        int x;
        printf("input: ");
        scanf("%d", &x);
        if(write(fd, &x, sizeof(int)) == -1){
            printf("write failed\n");
            return 2;
        }
        

        close(fd);
        exit(0);
    }else {
        
        int fd = open("myfifo", O_RDONLY);

        wait(NULL);
        int result;
        if(read(fd, &result, sizeof(int)) == -1){
            printf("read failed\n");
            return 3;
        }
        printf("received: %d\n", result);
        
    
        close(fd);
    }
    return 1;
    
}

int execPrac(){
    int pid = fork();
    if(pid == -1){
        printf("fork failed\n");
        return 1;
    }

    if(pid == 0){
        execlp("ping", "ping", "-c", "3", "google.com", NULL);
    }else {
        wait(NULL);
        printf("execution successful\n");
    }

    return 0;
}

void directOutputToFile(){
    int outputFile = open("outputFile.txt", O_WRONLY | O_CREAT, 0777);
    dup2(outputFile, STDOUT_FILENO);
    close(outputFile);
    execlp("ping", "ping", "-c", "3", "google.com", NULL);
}

void handle_sigcont(){
    printf("input x: \n");
    fflush(stdout);
}

void signalHandling(){
    struct sigaction sa;
    sa.sa_handler = &handle_sigcont;
    sa.sa_flags = SA_RESTART;
    sigaction(SIGCONT, &sa, NULL);

    int x;
    printf("input x:");
    fflush(stdout);
    scanf("%d", &x);
    printf("x is : %d", x);
}

void handle_sigusr1(){
    printf("\nit's 15!\n");
}

int pCommSig(){
    pid_t pid = fork();
    if(pid == -1){
        return 1;
    }
    if(pid == 0){
        //child process
        sleep(5);
        kill(getppid(), SIGUSR1);
        exit(0);
    }else{
        //parent process
        struct sigaction sa;
        sa.sa_handler = &handle_sigusr1;
        sa.sa_flags = SA_RESTART;
        sigaction(SIGUSR1, &sa, NULL);
        int x;
        printf("what is the result of 3 x 5: ");
        scanf("%d", &x);
        if(x == 15){
            printf("correct\n");
        }else{
            printf("incorrect\n");
        }
        kill(pid, SIGKILL);
        wait(NULL);
    }
    return 0;
}

//dynamically allocated memory
int memoryAllocation(){
    int* arr = malloc(sizeof(int)*256); //allocates a section of memory and returns the pointer to the memory 
    if(arr == NULL){ //memory allocation failed
        return 1;
    }
    memset(arr, 50, sizeof(int)*256);
    int i;
    for(i = 0; i<256; i++){
        printf("%d ", arr[i]);
    }
    free(arr);

    return 0;
}


int main(int argc, char* argv[])
{   
    int fileSize;
    char* msg = 0;
    FILE *pF = fopen(argv[1], "r");
    if(pF == NULL){
        printf("File Name/Path Not Valid");
        return 2;
    }

    fseek(pF, 0, SEEK_END);
    fileSize = ftell(pF);
    fseek(pF, 0, SEEK_SET);
    msg = malloc(fileSize);
    if (msg) {
        fread(msg, 1, fileSize, pF);
    }
    

    fclose(pF);
    printf("message: %s\n", msg);
    return 0;
}

