#define _GNU_SOURCE
#include <signal.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <sched.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>


#ifndef CHILD_SIG
#define CHILD_SIG SIGUSR1
#endif

static void errExit(const char* msg) {
  printf(msg);
  _exit(-1);
}

static int childFunc(void *args) {
  if (close(*((int *) args)) == -1 ) { // 1
    errExit("close");
  }
  return 0;
}

int main(int argc, char* argv[]) {
  const int STACK_SIZE = 65536;
  char *stack;
  char *stackTop;
  int s, fd, flags;

  fd = open("/dev/null", O_RDWR); // 2
  if (fd == -1)
    errExit("open");

  flags = (argc > 1) ? CLONE_FILES : 0; // 3

  stack = malloc(STACK_SIZE); // 4
  if (stack == NULL)
    errExit("malloc");

  stackTop = stack + STACK_SIZE;

  if (CHILD_SIG != 0 && CHILD_SIG != SIGCHLD) // 5
    if (signal(CHILD_SIG, SIG_IGN) == SIG_ERR)
      errExit("signal");

  if (clone(childFunc, stackTop, flags | CHILD_SIG, (void *) &fd) == -1) // 6
    errExit("clone");

  if (waitpid(-1, NULL, (CHILD_SIG != SIGCHLD) ? __WCLONE : 0) == -1) // 7
    errExit("waitpid");
  printf("child has terminated\n");

  s = write(fd, "x", 1); // 8
  if (s == -1 && errno == 9)
    printf("file descriptor %d has been closed\n", fd);
  else if (s == -1)
    printf("write() on file descriptor %d failed, errno: %d", fd, errno);
  else
    printf("write() on file descriptor %d succeeded\n", fd);

  exit(0);
}

  
