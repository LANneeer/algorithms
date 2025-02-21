#include <iostream>
using namespace std;
int main() {
	char arr[3] = {'a', 'b', 'c'};
	int i = 0;
	while (i < 3){
	cout << *(arr + i);
	i++;
	}
	cout << endl;
	return 0;
};
