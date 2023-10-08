# enum point
# count number of lines from said point, find total num and invalid

n, c = map(int, input().split())
points = list(map(int, input().split()))
count = [0] * c
for i in points: count[i] += 1
psa = [count[0]]
for i in range(1, 2 * c): psa.append(psa[-1] + count[i % c])
ans = [0, 0]
lines = [0, 0]  # all, impossible

for i in range(1, c):
    if i <= c // 2:
        lines[1] += count[i] * (psa[c // 2] - count[0] - count[i])
    lines[0] += count[i] * (psa[c - 1] - count[0] - count[i])

lines[0] = lines[0] // 2
lines[1] = lines[1] // 2

ans[0] += count[0] * lines[0]
ans[1] += count[0] * lines[1]

for i in range(1, c):
    lines[0] -= count[i] * (psa[c - 1] - count[i - 1] - count[i])
    lines[0] += count[i - 1] * (psa[c - 1] - count[i - 1] - count[i])
    lines[1] -= count[i] * (psa[c // 2 + i - 1] - psa[i])
    lines[1] += count[(c // 2 + i) % c] * (psa[c // 2 + i - 1] - psa[i])
    ans[0] += count[i] * lines[0]
    ans[1] += count[i] * lines[1]

print(ans[0] // 3 - ans[1])
