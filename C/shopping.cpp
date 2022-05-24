#include <bits/stdc++.h>

using namespace std;

int max_toys(int cost[], int N, int k){

	int sum = 0;
	int count = 0;


	for (int i = 0; i < N; i++){

		if ( sum + cost[i] <= k){
			sum = sum + cost[i];
			count++;
		}

	}
	return count;
}

int main(){

	int k;
	cout << "How much money do you have to spend? " << endl;
	cin >> k;

	//int k = 50;
	int cost[] = {10,11,12,13,20,25,50};
	int N = sizeof(cost) / sizeof(cost[0]);

	cout << "You can buy " << max_toys(cost, N, k) << " items with $" << k << "." << endl;
	return 0;

}
