#include<iostream>
#include<string>
#include<vector>

using namespace std;



template<typename T> T myMax(T x, T y) {

	return (x > y) ? x : y;
}


int main(){

	cout <<  myMax<int>(4, 10) << endl; 
	cout << myMax<float>(7.32, 3.34) << endl;	
	cout << myMax<char>('A', 'x') << endl;	
}
