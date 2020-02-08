#include <signal.h>
#include <libgen.h>
#include <stdio.h>
#include <stdlib.h>

#define CMD_SIZE 200

int main(int argc, char *argv[]) {
  char cmd[CMD_SIZE];
  pid_t childPid;

  setbuf(stdout, NULL);
  printf("Parent PID=%ld\n", (long) getpid());

  switch (childPid = fork()) {
  case -1:
    printf("error");
    exit(-1);
  case 0:
    printf("Child (PID=%ld) exiting\n", (long) getpid());
    _exit(0);
  default:
    sleep(3);
    snprintf(cmd, CMD_SIZE, "ps aux| grep %s", basename(argv[0]));
    cmd[CMD_SIZE-1] = '0';
    system(cmd);

    if (kill(childPid, SIGKILL) == -1) {
      printf("error kill");
      exit(-1);
    }
    sleep(3);
    printf("After sending SIGKILL to zombie (PID=%ld):\n", (long) childPid);
    system(cmd);
    exit(0);
  }
}
