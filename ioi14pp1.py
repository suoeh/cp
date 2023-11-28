n = int(input())
grid = [['0'] * (n + 1)]
dp = [[0] * (n + 1)]

value = 0
counter = 0

for i in range(n):
    grid.append(['0'])
    grid[i + 1] += list(input().replace(' ', ''))
    dp.append([0] + [1] * n)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if grid[i][j] == '0':
            dp[i][j] = 0
        else:
            if grid[i - 1][j] != '0' and grid[i][j - 1] != '0' and grid[i - 1][j - 1] != '0':
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                if grid[i - dp[i][j] + 1][j - dp[i][j] + 1] == '0': dp[i][j] -= 1
        value = max(value, dp[i][j])
        
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dp[i][j] == value:
            counter += 1

print(value * counter)
