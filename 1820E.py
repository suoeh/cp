import sys

input = sys.stdin.readline


def solve():
    r, c = map(int, input().split())
    grid = []
    ans = 0

    for _ in range(r):
        grid.append(list(map(int, input().split())))

    for i in range(r):
        for j in range(c):
            temp = 0
            if grid[i][j] == 0:
                continue

            stack = [(i, j)]
            while stack:
                row, column = stack.pop()
                if row >= r or column >= c or column < 0 or row < 0:
                    continue
                if grid[row][column] == 0:
                    continue

                temp += grid[row][column]
                grid[row][column] = 0

                stack.append((row + 1, column))
                stack.append((row - 1, column))
                stack.append((row, column + 1))
                stack.append((row, column - 1))

            ans = max(ans, temp)

    return ans


for _ in range(int(input())):
    print(solve())
