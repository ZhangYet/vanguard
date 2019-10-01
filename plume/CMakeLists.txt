project(plume)


set(plume_VERSION_MAJOR, 0)
set(plume_VERSION_MINOR, 1)

include_directories("/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/")

add_executable(atomic_append atomic_append/append.c)
add_executable(view_symlink realpath/view_link.c)