#include <ftw.h>
#include <sys/inotify.h>

int INOTIFY_INST;

int addInotify(const char *pathname, const struct stat *sbuf, int type, struct FTW *ftwb)
{
  int desc;
  desc = inotify_add_watch(INOTIFY_INST, pathname, IN_ALL_EVENTS);
  if (desc > 0) {
    return 0;
  }
  return -1;
}

int iterDir(const char *pathname)
{
  int ret = nftw(pathname, addInotify, 10, 0);
  return ret
}  
