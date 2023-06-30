#include <bits/stdc++.h>
using namespace std;
#define int long long
#define watch(x) cerr << (#x) << " is " << (x) << "\n";
#define all(x) (x).begin(), (x).end()
#define sz(a) (int)(a).size()
#define vi vector<int>
#define pii pair<int, int>
#define fi first
#define se second

// const int maxn = max n for array
const int maxn = 300001;
// variables go here
int n, a[maxn];

void solve() {
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];
    int ans = 1;
    string mode = "?";
    for (int i = 2; i <= n; i++){
        string next = "?";
        if (a[i-1] > a[i]) next = "1";
        if (a[i-1] < a[i]) next = "2";
        if (next == "?") continue;
        if (next != mode) ans++;
        mode = next;
    }
    cout << ans << "\n";
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while(t--) solve();
}
