import sys

input = sys.stdin.readline

n, l, s = map(int, input().split())
ans = l
level = 0
points = [[1, 0]]

for _ in range(n):
    left, right, v = map(int, input().split())
    points.append([left, v])
    points.append([right + 1, -v])

points.append([l, 0])
points.sort()

for i in range(1, 2 * (n + 1)):
    level += points[i][1]
    if level >= s:
        ans -= points[i + 1][0] - points[i][0]

print(ans)
