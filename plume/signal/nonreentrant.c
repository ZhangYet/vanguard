//
// Created by 张晔 on 2020/1/11.
//

#include <unistd.h>
#include <signal.h>
#include <string.h>
#include <stdio.h>

static char *str2;
static int handled = 0;
void handler(int sig)
{
    
    crypt(str2, "xx");
    handled ++;
}

int main(int argc, char *argv[])
{
    
    char *cr1;
    int callNum, mismath;
    struct sigaction sa;
    
    if (argc != 3) {
        printf("%s str1 str2\n", argv[0]);
        _exit(-1);
    }

    str2 = argv[2];
    cr1 = strdup(crypt(argv[1], "xx"));
    
    if (cr1 == NULL) {
        printf("strdup");
        _exit(-1);
    }
    
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;
    sa.sa_handler = handler;
    
    if (sigaction(SIGINT, &sa, NULL) == -1) {
        printf("sigaction");
        _exit(-1);
    }
    
    for (callNum = 1, mismath = 0; ; callNum++) {
        if ((strcmp(crypt(argv[1], "xx"), cr1) != 0)) {
            mismath ++;
            printf("Mismatch on call %d (mismatch=%d, handled=%d)\n", callNum, mismath, handled);
        }
    }
}