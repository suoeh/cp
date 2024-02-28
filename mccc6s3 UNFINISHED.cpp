#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("Ofast", "unroll-loops")
template<typename _Tp> using maxq = priority_queue<_Tp>;
template<typename _Tp> using minq = priority_queue<_Tp, vector<_Tp>, greater<_Tp>>;
#define lc (rt<<1)
#define rc (rt<<1|1)
#define cl(a, b) memset(a, b, sizeof(a))
#define mp(a, b) make_pair((a), (b))
#define watch(x) cerr << (#x) << " is " << (x) << "\n";
#define all(x) (x).begin(), (x).end()
#define sz(a) (int)(a).size()
#define vi vector<int>
#define pii pair<int, int>
#define fi first
#define se second
#define pb push_back
#define scan(x){for(x=*_ii++-'0'; *_ii++>='0'; x=x*10+_ii[-1]-'0');}
#define min(a,b) a < b ? a : b
#define max(a,b) a > b ? a : b
#define int long long

const int mx = 10e6+2;
int arr[mx];
int psa[mx];
int values[2];

void solve() {
    int n, ideal, temp, temp2, t, ind;
    cin >> n;
    multiset<int> left;
    multiset<int> right;
    for(int i=0;i<n;i++){
        cin >> arr[i];
        psa[i + 1] = psa[i] + arr[i];
        right.insert(arr[i]);
    }
    right.erase(right.lower_bound(arr[0]));
    if (right.count(arr[0]) == 0){
        right.erase(arr[0]);
    }
    for(int i=0; i<n;i++){
        values[0] = psa[i];
        values[1] = psa[n] - psa[i + 1];

        ideal = (values[1] - values[0]) / 2;
        if(values[1] > values[0]){
            temp = abs(*right.upper_bound(ideal) - ideal);
            temp2 = abs(*right.lower_bound(ideal) - ideal);
            if(temp > temp2){
                values[]
            }
        }
        ans = min(ans, values[1] - values[0]);

        cout << values[0] << " " << values[1] << '\n';
    }

}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
}
