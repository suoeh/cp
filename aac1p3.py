def solve():
    n, x = map(int, input().split())

    if (n - x) % 2 != 0:
        return [-1]

    ans = [0] * n

    for i in range(0, n - x, 2):
        ans[i] = 1

    return ans


print(*solve())
