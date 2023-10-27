import sys

input = sys.stdin.readline

r, c = map(int, input().split())
psa = [[0] * (c + 1)]

for i in range(1, r + 1):
    string = [*''.join(input())]
    for j in range(c):
        if string[j] == "X":
            string[j] = 1
        else:
            string[j] = 0
    psa.append([0] + string)

for i in range(1, r + 1):
    for j in range(1, c + 1):
        psa[i][j] += psa[i][j - 1]
        psa[i][j] += psa[i - 1][j]
        psa[i][j] -= psa[i - 1][j - 1]


def check(s):
    global r, c, psa
    visited = []
    for _ in range(r - s + 1):
        visited.append([False] * (c - s + 1))
    stack = [(0, 0)]

    while stack:
        ro, co = stack.pop()
        if psa[ro + s][co + s] - psa[ro + s][co] - psa[ro][co + s] + psa[ro][co] > 0:
            continue

        if ro == r - s and co == c - s:
            return True

        if ro + 1 <= r - s:
            if not visited[ro + 1][co]:
                visited[ro + 1][co] = True
                stack.append((ro + 1, co))
        if ro - 1 >= 0:
            if not visited[ro - 1][co]:
                visited[ro - 1][co] = True
                stack.append((ro - 1, co))
        if co + 1 <= c - s:
            if not visited[ro][co + 1]:
                visited[ro][co + 1] = True
                stack.append((ro, co + 1))
        if co - 1 >= 0:
            if not visited[ro][co - 1]:
                visited[ro][co - 1] = True
                stack.append((ro, co - 1))

    return visited[-1][-1]


left = 1
right = min(r, c)
ans = 0

while left <= right:
    m = (left + right) // 2
    if check(m):
        left = m + 1
        ans = max(ans, m)
    else:
        right = m - 1

print(ans)
