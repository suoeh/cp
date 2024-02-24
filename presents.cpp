#include <bits/stdc++.h>
using namespace std;
#define watch(x) cerr << (#x) << " is " << (x) << "\n";
#define all(x) (x).begin(), (x).end()
#define sz(a) (int)(a).size()
#define vi vector<int>
#define pii pair<int, int>
#define fi first
#define se second
#define FOR(i, s, e) for(int i = s, i <= e, i++)
#define int long long

int n, c, temp;
multiset<int> presents;

int solve() {
    cin >> n;
    int ans = 0;
    vector<int> child(n);
    for(int i = 0; i < n; i += 1){
        cin >> child[i];
    }

    cin >> c;
    for(int i = 0; i < c; i += 1){
        cin >> temp;
        presents.insert(temp);
    }

    sort(all(child));

    for(int i = n - 1; i >= 0; i -= 1){
        if (child[i] < *presents.begin()){
            return -1;
        }

        auto it = presents.upper_bound(child[i]);
        it--;

        ans += child[i] - *it;

        presents.erase(it);
    }

    return ans;
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cout << solve();
}
