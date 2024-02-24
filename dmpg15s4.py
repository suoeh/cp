import sys

input = sys.stdin.readline
from collections import deque

mii = lambda: map(int, input().split())


# idea: create adj list, o(n^2)
# bfs queries

def solve():
    b, q = mii()
    arr = [list(mii()) for _ in range(b)]
    adj = [[] for _ in range(b + 1)]

    queue = deque([])

    for _ in range(q):
        found = False
        start, end = mii()
        queue.append(start)
        vis = [False for _ in range(b + 1)]
        vis[start] = True

        while queue:
            n = queue.popleft()
            if n == end:
                found = True
                queue.clear()
                break

            for i in range(b):
                if i == n - 1: continue
                if vis[i + 1]: continue
                dist = (arr[i][0] - arr[n - 1][0]) ** 2 + (arr[i][1] - arr[n - 1][1]) ** 2
                if dist <= arr[n - 1][2] ** 2:
                    queue.append(i + 1)
                    vis[i + 1] = True

        print("YES" if found else "NO")


solve()
