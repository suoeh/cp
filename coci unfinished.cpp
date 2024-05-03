#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
#define print(arr, n){cerr << #arr; for(int _i = 0; _i < (n); _i++) cerr << ' ' << (arr)[_i]; cerr << endl;}
#define nl '\n'
#define int long long

int base(int n, int s) {
    int dp[16][136];
    dp[0][0] = 1;
    int l = (int) log10(n);
    for (int i = 0; i < l - 1; i++) {
        for (int j = 0; j <= s; j++) {
            int cur = dp[i][j];
            for (int k = 0; k < 10; k++) {
                if (j + k > s) {
                    break;
                }
                dp[i + 1][j + k] += cur;
            }
        }
    }

    int digit = n % (int) pow(10, l);

    for (int j = 0; j <= s; j++) {
        int cur = dp[l - 1][j];
        for (int k = 1; k < digit; k++) {
            if (j + k > s) {
                break;
            }
            dp[l][j + k] += cur;
        }
    }

    return dp[l][s];
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int a, b, s;
    cin >> a >> b >> s;
    int aa = 0, ab = 0;

    cout << base(b, s) << nl;

}
