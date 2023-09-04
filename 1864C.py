import sys
from math import log

input = sys.stdin.readline


def solve():
    n = int(input())
    ans = [n]
    pow = int(log(n, 2))
    target = 2 ** pow

    if n % 2 == 1:
        n -= 1
        ans.append(n)

    diff = n - target
    v = []

    for i in range(pow, 0, -1):
        if diff - 2 ** i >= 0:
            diff -= 2 ** i
            v.append(2 ** i)

    v.sort()

    for i in v:
        n -= i
        ans.append(n)

    while n != 1:
        n //= 2
        ans.append(n)

    print(len(ans))

    return ans


for _ in range(int(input())):
    print(*solve())
