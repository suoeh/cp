#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
#pragma GCC optimize("Ofast", "unroll-loops")
#define all(x) (x).begin(), (x).end()
#define len(x) (int)(x).size()
#define vi vector<int>
#define pii pair<int, int>
#define print(arr, n){cerr << #arr; for(int _i = 0; _i < (n); _i++) cerr << ' ' << (arr)[_i]; cerr << endl;}
#define nl '\n'
#define int long long

const int inf = 0x3f3f3f3f;
const int MOD = 1e9+7;
const int mx = 2e5+5;

int n, query;
vector<vi> graph(mx);
vi dist(mx, -1);
vi path;
vector<vi> ext(mx);

void dfs(int cur, int depth) {
    if (dist[cur] != -1)
        return;
    dist[cur] = depth;
    for (auto& u : graph[cur]) {
        dfs(u, depth + 1);
    }
}

void dfs2(int cur, int depth, int target) {
    path.push_back(cur);
    if (dist[cur] != -1)
        return;
    dist[cur] = depth;
    if (cur == target) {
        print(path, n)
        return;
    }
    for (auto& u : graph[cur]) {
        dfs2(u, depth + 1, target);
    }
    path.pop_back();
}

void pathfind(int start, int end) {
    
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n;
    int s, e;
    for (int i = 0; i < n - 1; i++) {
        cin >> s >> e;
        graph[s].push_back(e);
        graph[e].push_back(s);
    }

    dfs(1, 0);

    int cur = 0;
    int index = 0;
    for (int i = 1; i <= n; i++) {
        if (dist[i] > cur) {
            index = i;
            cur = dist[i];
        }
    }

    fill(all(dist), -1);
    dfs(index, 0);

    cur = 0;
    int index2 = 0;
    for (int i = 1; i <= n; i++) {
        if (dist[i] > cur) {
            index2 = i;
            cur = dist[i];
        }
    }

    fill(all(dist), -1);


}
