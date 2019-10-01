//
// Created by 张晔 on 2019/10/1.
//
#include <string.h>
#include <sys/stat.h>
#include <stdio.h>
#include <zconf.h>
#include <stdlib.h>

#define BUF_SIZE 4096

int main(int argc, char *argv[]) {
    struct stat statbuf;
    char buf[BUF_SIZE];
    ssize_t numBytes;
    if (argc != 2 || strcmp(argv[1], "--help") == 0)
        printf("%s pathname\n", argv[0]);
    if (lstat(argv[1], &statbuf) == -1) {
        printf("error when lstat");
        exit(EXIT_FAILURE);
    }

    if (!S_ISLNK(statbuf.st_mode)) {
        printf("%s is not a symbolic link", argv[1]);
    }

    numBytes = readlink(argv[1], buf, BUF_SIZE-1);
    if (numBytes == -1) {
        printf("error when readlink");
        exit(EXIT_FAILURE);
    }

    buf[numBytes] = '\0';
    printf("readlink: %s --> %s\n", argv[1], buf);

    if (realpath(argv[1], buf) == NULL) {
        printf("error when realpath");
        exit(EXIT_FAILURE);
    }
    printf("realpath: %s --> %s \n", argv[1], buf);

    exit(EXIT_SUCCESS);


}
