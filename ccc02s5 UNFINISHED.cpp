#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("Ofast", "unroll-loops")
#define watch(x) cerr << (#x) << " is " << (x) << "\n";
#define all(x) (x).begin(), (x).end()
#define sz(a) (int)(a).size()
#define vi vector<int>
#define pii pair<int, int>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define scan(x){for(x=*_ii++-'0'; *_ii++>='0'; x=x*10+_ii[-1]-'0');}
#define min(a,b) a < b ? a : b
#define max(a,b) a > b ? a : b

pii simulate(int w, int h, int x, int y, int d) {
    if (d == 0) {
        if (h - y > w - x) {
            return {x + w - x, y + w - x};
        }
        return {x + h - y, y + h - y};
    } else if (d == 1) {
        if (h - y < x) {
            return {x - h - y, y + h - y};
        }
        return {x - x, y - x};
    } else if (d == 2) {
        if (y > x) {
            return {x - x, y - x};
        }
        return {x - y , y - y};
    }
    if (w - x > y) {
        return {x - y, y - y};
    }
    return {x + w - x , y + w - x};
}

void solve() {
    int w, h, x, y, d = 0; // up right,  left, down left, down right
    cin >> w >> h >> x >> y;

    int ans = 0;
    bool coord[w][h];
    for (int i = 0; i < w; i++) {
        for (int j = 0; j < h; j++) {
            coord[i][j] = true;
        }
    }

    coord[x][y] = true;

    while (1) {
        pii temp = simulate(w, h, x, y, d);
        x = temp.fi;
        y = temp.se;
        d++;
        d %= 4;

        if (coord[x][y] = true) {
            cout << 0;
            return;
        }

        coord[x][y] = true;

        if (x < 5 and y < 5) {
            cout << ans; return;
        }
        if (x > (w - 5) and y < 5) {
            cout << ans; return;
        }
        if (x < 5 and y < 5) {
            cout << ans; return;
        }
        if (x < 5 and y > (h - 5)) {
            cout << ans; return;
        }
        ans++;

    }

}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
}
