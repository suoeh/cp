import heapq
import sys
from collections import deque

input = sys.stdin.readline


# MOD = 10 ** 9 + 7


def solve():
    n, w, d = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    vis = [False] * (n + 1)
    for _ in range(w):
        s, e = map(int, input().split())
        adj[e].append(s)

    route = list(map(int, input().split()))
    dist = dict()
    queue = deque([(n, 0)])

    while queue:
        node, depth = queue.popleft()
        if vis[node]: continue
        vis[node] = True
        dist[node] = depth
        for i in adj[node]:
            queue.append((i, depth + 1))

    for i in range(n):
        temp = route[i]
        if temp in dist.keys():
            route[i] = dist[temp]
        else:
            route[i] = 200001

    ans = [i + route[i] for i in range(n)]
    pq = ans[:]
    heapq.heapify(pq)
    invalid = [0] * 200001

    for _ in range(d):
        left, right = map(int, input().split())

        if ans[left - 1] <= 200000:
            invalid[ans[left - 1]] += 1
        if ans[right - 1] <= 200000:
            invalid[ans[right - 1]] += 1

        ans[left - 1] += - route[left - 1] + route[right - 1]
        ans[right - 1] += - route[right - 1] + route[left - 1]
        route[left - 1], route[right - 1] = route[right - 1], route[left - 1]

        if ans[left - 1] <= 200000:
            heapq.heappush(pq, ans[left - 1])
        if ans[right - 1] <= 200000:
            heapq.heappush(pq, ans[right - 1])

        while True:
            temp = pq[0]
            if invalid[temp] == 0:
                print(temp)
                break
            invalid[temp] -= 1
            heapq.heappop(pq)


solve()
