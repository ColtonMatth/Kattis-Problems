//Name: Colton Matthews
//File: geppetto.cpp
//Date: 10/13/2022

#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
	int n, m; 
    int a, b;
	cin >> n >> m;
	unordered_set<int> masks;
	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		a--; 
        b--;
		masks.insert((1 << a) | (1 << b));
	}

	int count = 0;
    bool good;
	for (int i = 0; i < (1 << n); i++) {
		good = true;
		for (auto m : masks) {
			if ((i & m) == m) {
				good = false;
				break;
			}
		}

		if (good)
			count++;
	}

	cout << count;
}