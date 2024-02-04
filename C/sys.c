#include <stdio.h>
#include <stdlib.h>
#include <sys/sysinfo.h>
#include <unistd.h>
#include <sys/utsname.h>

void getSystemInfo() {
    // Get system information
    struct sysinfo sys_info;
    if (sysinfo(&sys_info) != 0) {
        perror("Error getting system information");
        exit(EXIT_FAILURE);
    }

    // Print system information
    printf("OS Type: %s\n", sys_info.uptime > 0 ? "Linux" : "Other");
    printf("Total RAM: %ld MB\n", sys_info.totalram / (1024 * 1024));
    printf("Free RAM: %ld MB\n", sys_info.freeram / (1024 * 1024));

    // Use 'uname' to get system information
    struct utsname uname_info;
    if (uname(&uname_info) == 0) {
        printf("System Name: %s\n", uname_info.sysname);
        printf("Node Name: %s\n", uname_info.nodename);
        printf("Release: %s\n", uname_info.release);
        printf("Version: %s\n", uname_info.version);
        printf("Machine: %s\n", uname_info.machine);
    } else {
        perror("Error getting system information");
        exit(EXIT_FAILURE);
    }
}

int main() {
    getSystemInfo();
    return 0;
}
