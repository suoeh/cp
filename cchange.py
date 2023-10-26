import sys
from collections import deque

stack = deque([[int(input()), 0]])
coins = []
visited = [False] * 10001
for _ in range(int(input())):
    coins.append(int(input()))

while stack:
    temp, value = stack.popleft()
    visited[temp] = True
    for i in coins:
        if temp - i > 0 and not visited[temp - i]:
            stack.append([temp - i, value + 1])
            visited[temp - i] = True
        if temp - i == 0:
            print(value + 1)
            sys.exit()
