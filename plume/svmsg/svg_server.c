//
// Created by 张晔 on 2020/2/21.
//

#include "svg.h"

static void grimReaper(int sig) {
    int savedErrno;

    savedErrno = errno;
    while (waitpid(-1, NULL, WNOHANG) > 0)
        continue;
    errno = savedErrno;
}

static void serveReq(const struct requestMsg *req) {
    int fd;
    ssize_t numRead;
    struct responseMsg resp;

    fd = open(req->pathname, O_RDONLY);
    if (fd == -1) {
        resp.mtype = RESP_MT_FAILURE;
        snprintf(resp.data, sizeof(resp.data), "%s", "couldn't open");
        msgsnd(req->clientId, &resp, strlen(resp.data)+1, 0);
        exit(EXIT_FAILURE);
    }

    resp.mtype = RESP_MT_DATA;
    while ((numRead = read(fd, resp.data, REQ_MSG_SIZE)) > 0)
        if (msgsnd(req->clientId, &resp, numRead, 0) == -1)
            break;

    resp.mtype = RESP_MT_END;
    msgsnd(req->clientId, &resp, 0, 0);
}

static void errExit(const char *msg) {
    printf(msg);
    exit(-1);
}

int main(int argc, char *argv[]) {
    struct requestMsg req;
    pid_t pid;
    ssize_t  msgLen;
    int serverId;
    struct sigaction sa;

    serverId = msgget(SERVER_KEY, IPC_CREAT|IPC_EXCL|
                        S_IRUSR|S_IWUSR|S_IRGRP);
    if (serverId == -1)
        errExit("msgget");

    sigemptyset(&sa.sa_mask);
    sa.sa_flags = SA_RESTART;
    sa.sa_handler = grimReaper;
    if (sigaction(SIGCHLD, &sa, NULL) == -1)
        errExit("sigaction");

    for(;;) {
        msgLen = msgrcv(serverId, &req, REQ_MSG_SIZE, 0,0);
        if (msgLen == -1) {
            if (errno == EINTR)
                continue;
            printf("msgrcv");
            break;
        }

        pid = fork();
        if (pid == -1) {
            serveReq(&req);
            _exit(EXIT_SUCCESS);
        }
    }
    if (msgctl(serverId, IPC_RMID, NULL) == -1)
        errExit("msgctl");
    exit(EXIT_SUCCESS);
}