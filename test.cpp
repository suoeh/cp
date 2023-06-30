#include <bits/stdc++.h>
using namespace std;

int main() {
    int k, n, w, value, owe;
    value = 0;
    cin >> k >> n >> w;
    for(int i = 1; i <= w; i++){
        value += k * i;
    }
    owe = (value < n)? 0:value - n;
    cout << owe;
}
