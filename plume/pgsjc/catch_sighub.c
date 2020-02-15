#define _XOPEN_SOURCE 500
#include <unistd.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>

static void hander(int sig) {}

static void errExit(const char* msg) {
  printf(msg);
  exit(-1);
}

int main(int argc, char *argv[]) {
  pid_t childPid;
  struct sigaction sa;

  setbuf(stdout, NULL);

  sigemptyset(&sa.sa_mask);
  sa.sa_flags = 0;
  sa.sa_handler = hander;

  if (sigaction(SIGHUP, &sa, NULL) == -1)
    errExit("sigaction");

  childPid = fork();
  if (childPid == -1)
    errExit("fork");

  if (childPid == 0 && argc > 1)
    if (setpgid(0, 0) == -1)
      errExit("setpgid");

  printf("PID=%ld, PPID=%ld, PGID=%ld, SID=%ld\n",
	 (long) getpid(), (long) getppid(),
	 (long) getpgrp(), (long) getsid(0));

  alarm(60);

  for(;;) {
    pause();
    printf("%ld: caught SIGHUP\n", (long) getpid());
  }
}
