#include<stdio.h>
#include<string.h>

typedef struct Persons {
	char fname[50];
	char lname[50];
	int age;
} Person;

int main (){

	int i=0, j, n;

	Person c;

	printf("Enter the value: ");
	scanf("%d", &n);
	printf("Enter your name: ");
	scanf("%s %s", &c.fname, &c.lname);
	printf("Enter your age: ");
	scanf("%d", &c.age);

	do {

		printf("%d\n", i);
		i++;

	} while (i < n);


	printf("My name is: %s %s and my age is %d\n", c.fname, c.lname, c.age);

	return 0;

}
