import sys

input = sys.stdin.readline
print = sys.stdout.write


def solve():
    n, k = map(int, input()[:-1].split())
    t = list(input().strip())

    if k % 2 == 0:
        t.sort()
        return t

    l = [[t[i] for i in range(0, n, 2)], [t[i] for i in range(1, n, 2)]]
    ans = []

    l[0].sort()
    l[1].sort()

    for i in range(len(l[0])):
        ans.append(l[0][i])
        if i < len(l[1]):
            ans.append(l[1][i])

    return ans


for _ in range(int(input())):
    print(''.join(solve()) + ' ')
