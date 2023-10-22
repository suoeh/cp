house, road, a, b = map(int, input().split())
adj = []
for i in range(house + 1):
    adj.append([])

visited = set()
visited.add(a)
for _ in range(road):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

stack = []
for i in adj[a]:
    stack.append(i)

while stack:
    temp = stack.pop(0)
    visited.add(temp)
    for i in adj[temp]:
        if i not in visited and i not in stack:
            stack.append(i)

if b in visited:
    print('GO SHAHIR!')
else:
    print('NO SHAHIR!')
