#include<stdio.h>

    int main() {
        int num = 42;       // Declare an integer variable
        int *ptr = &num;    // Declare a pointer to an integer and assign the address of 'num' to it

        printf("Value of num: %d\n", *ptr);     // Access the value using the pointer
        printf("Memory address of num: %p\n", ptr);   // Access the memory address


        return 0;
}

