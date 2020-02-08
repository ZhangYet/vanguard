#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  printf("hello world\n");
  write(STDOUT_FILENO, "Ciao\n", 5);
  if (fork() == -1) {
    printf("fork error");
    _exit(-1);
  }
  _exit(0);
}
