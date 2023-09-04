# input = sys.stdin.readline
# print = sys.stdout.write


def solve():
    x, y, n = map(int, input().split())

    if y - x < (n - 1) * n // 2:
        return [-1]

    ans = [y for _ in range(n - 1)]

    for i in range(n - 1):
        ans[i] -= i * (i + 1) // 2

    ans.reverse()
    ans = [x] + ans

    return ans


for _ in range(int(input())):
    print(*solve())
