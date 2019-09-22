project(plume)


set(plume_VERSION_MAJOR, 0)
set(plume_VERSION_MINOR, 1)

include_directories("/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/")

add_executable(plume, simple-cp/cp.c)