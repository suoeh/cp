import sys

input = sys.stdin.readline

r = int(input())
c = int(input())
adj = [[] for _ in range(1000001)]
visited = []
for i in range(r):
    temp = list(map(int, input().split()))
    visited.append([False] * c)
    for j in range(c):
        adj[temp[j]].append((i + 1, j + 1))

stack = [(r, c)]
visited[r - 1][c - 1] = True

while stack:
    row, column = stack.pop()
    if row == 1 and column == 1: break
    for i in adj[row * column]:
        if not visited[i[0] - 1][i[1] - 1]:
            visited[i[0] - 1][i[1] - 1] = True
            stack.append(i)

print("yes") if visited[0][0] else print("no")
