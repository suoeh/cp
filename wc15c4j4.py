import bisect
import math
import sys

input = sys.stdin.readline
mii = lambda: map(int, input().split())


def solve():
    n, k = mii()
    ans = [0, 0]
    rings = [0] * n
    scores = [0] * n
    shots = [0] * n

    for i in range(n):
        rings[i] = int(input())
    for i in range(n):
        scores[i] = int(input())
    scores.sort()

    for i in range(k):
        x, y = mii()
        dist = math.sqrt(x ** 2 + y ** 2)
        num = bisect.bisect_left(rings, dist)
        if num < n:
            shots[num] += 1

    shots.sort()

    for i in range(n):
        ans[0] += shots[i] * scores[n - i - 1]
        ans[1] += shots[i] * scores[i]

    print(ans[0])
    print(ans[1])


solve()
