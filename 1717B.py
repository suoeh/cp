import sys

input = sys.stdin.readline


def solve():
    n, k, c, r = map(int, input().split())

    r = r % k
    c = c % k

    if r == 0: r = k
    if c == 0: c = k

    up = (r - c) % k  # diff

    base = "X" + "." * (k - 1)
    tile = []

    for i in range(k, 0, -1):
        tile.append(base[i % k:] + base[:i % k])

    tile = tile[up % k:] + tile[:up % k]

    for i in range(k):
        tile[i] = tile[i] * (n // k)

    for i in range(n // k):
        for j in range(k):
            print(tile[j])


for _ in range(int(input())):
    solve()
