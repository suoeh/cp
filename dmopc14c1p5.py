from collections import deque

r, c = map(int, input().split())
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
grid = []
visited = []
ans = [0, 0]  # dist to end, dist to nearest t
check = [False, False]
for i in range(r):
    grid.append(list(input()))
    visited.append([False] * c)
for i in range(int(input())):
    row, column = map(int, input().split())
    grid[row][column] = "T"

stack = deque([(sx, sy, 0)])
while stack:
    row, column, depth = stack.popleft()
    visited[row][column] = True

    if row == ey and column == ex and not check[0]:
        ans[0] = depth
        check[0] = True
    if grid[row][column] == "T" and not check[0]:
        ans[1] = depth
        check[1] = True

    if check[0] and check[1]:
        break

    if row - 1 >= 0 and grid[row - 1][column] != "X":
        if not visited[row - 1][column]:
            stack.append((row - 1, column, depth + 1))
    if row + 1 < r and grid[row + 1][column] != "X":
        if not visited[row + 1][column]:
            stack.append((row + 1, column, depth + 1))
    if column - 1 >= 0 and grid[row][column - 1] != "X":
        if not visited[row][column - 1]:
            stack.append((row, column - 1, depth + 1))
    if column + 1 < c and grid[row][column + 1] != "X":
        if not visited[row][column + 1]:
            stack.append((row, column + 1, depth + 1))

print(max(ans[0] - ans[1], 0))
