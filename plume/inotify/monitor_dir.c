#include <signal.h>
#include <stdio.h>

static void sigHandler(int sig)
{
  static int count = 0;

  if (sig == SIGINT) {
    count++;
    printf("Caught SIGINT (%d)\n", count);
    return;
  }

  printf("Caught SIGQUIT - that's all folks!\n");
  exit(0);
}

int main(int argc, char *argv[])
{
  if (signal(SIGINT, sigHandler) == SIG_ERR)
    exit(-1);

  if (signal(SIGQUIT, sigHandler) == SIG_ERR)
    exit(-1);

  for(;;)
    pause();
}
