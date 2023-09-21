import sys

read = sys.stdin.readline
write = sys.stdout.write


# MOD = 10 ** 9 + 7


def solve():
    n, k = map(int, read().split())
    arr = list(''.join(input()))
    ans = 0
    ban = 0

    for i in range(n):
        ban -= 1
        if ban > 0:
            continue
        if arr[i] == "B":
            ban = k
            ans += 1

    return ans


for _ in range(int(read())):
    write(str(solve()) + "\n")
