//
// Created by dantezy on 2019/9/22.
//

#include <fcntl.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

extern char **environ;

int main(int argc, char *argv[]) {
    char **ep;
    for (ep = environ; *ep != NULL; ep++ ) {
        printf("environ: %s\n", *ep);
    }

    bool is_append = true;
    printf("argc: %d, argv[3]: %s\n", argc, argv[3]);
    if (argc > 3 && strcmp(argv[3], "x") == 0) {
        is_append = false;
    }
    char *to_write = "x";
    if (argc > 4) {
        to_write = argv[4];
    }
    int byte_to_write = atoi(argv[2]);

    int fd;
    if (is_append) {
        printf("is append\n");
        fd = open(argv[1], O_WRONLY | O_CREAT | O_APPEND, 0644);
    } else {
        fd = open(argv[1], O_WRONLY | O_CREAT, 0644);
    }
    if (fd == -1) {
        printf("cannot open file %s\n", argv[1]);
        exit(-1);
    } else {
        printf("fd: %d\n", fd);
    }

    for (int i = 0; i < byte_to_write; i++) {
        int written = write(fd, to_write, strlen(to_write));
        if (written == -1) {
            printf("write failed\n");
            exit(-1);
        }
    }

    close(fd);
    exit(0);
}