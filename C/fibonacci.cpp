#include <iostream>

using namespace std;


int main() {
	int n, t1 = 0, t2 = 1, nextNum = 0;

	cout << "Enter the length of numbers: ";
	cin >> n;

	cout << "Fibonacci Series: ";

	for (int i = 1; i < n; i++) {
		if (i == 1) {
			cout << t1 << ",";
			continue;
		}
		if (i == 2) {
			cout << t2 << ",";
		}

		nextNum = t1 + t2;
		t1 = t2;
		t2 = nextNum;
		cout << nextNum << ",";
	}
	cout << endl;
	return 0;
}
