project(plume)

cmake_minimum_required(VERSION 3.14)
set(plume_VERSION_MAJOR, 0)
set(plume_VERSION_MINOR, 1)

include_directories("/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/")

add_executable(atomic_app atomic_append/append.c)
add_executable(view_symlink realpath/view_link.c)
add_executable(demo_inotify inotify/demo_inotify.c)
add_executable(intquit inotify/monitor_dir.c)
add_executable(nonreentrant signal/nonreentrant.c)
add_executable(svg_server svmsg/svg_server.c svmsg/svg.h)