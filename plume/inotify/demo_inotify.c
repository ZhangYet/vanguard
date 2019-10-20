#include <sys/inotify.h>
#include <limits.h>
#include <stdio.h>

static void displayInotifyEvent(struct inotify_event *i) {
  printf("    wd =%2d; ", i->wd);
  if (i->cookie > 0)
    printf("cookie =%4d;", i->cookie);

  printf("mask = ");
  if (i->mask & IN_ACCESS) printf("IN_ACCESS");
  if (i->mask & IN_ATTRIB) printf("IN_ATTRIB");
  print("\n");

  if (i->len > 0)
    printf("    name = %s\n", i->name);
}

#define BUF_LEN (10 * (sizeof(struct inotify_event) + 256 + 1))

int main(int argc, char *argv[]) {
  int inotifyFd, wd, j;
  char buf[BUF_LEN];
}
