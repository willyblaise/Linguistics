#include<stdio.h>

void swap(int a, int b);


void swap(int a, int b){
	int temp;

	if (a > b) {
		temp = a;
		a = b;
		b = temp;
		printf("%d and %d after swap\n", a, b);
	} else {
		printf("No swap necessary here: %d and %d\n", a, b);

	}
}

int main(){
	int c, d;

	printf("please enter first digit: "); scanf("%d", &c);
	printf("please enter first digit: "); scanf("%d", &d);

	swap(c, d);

}
