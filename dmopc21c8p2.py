import sys
n, m = map(int, input().split())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
possible = [[2, 2 * m], [2, 2 * m]]
ans = [0, 0]
zeroes = [0, 0]

for i in range(n):  # max min, min max
    mode = i % 2
    if row1[i] == 0 or row2[i] == 0:
        if row1[i] == 0 and row2[i] == 0:
            zeroes[mode] += 1
            possible[mode][0] = max(possible[mode][0], 2)
            possible[mode][1] = min(possible[mode][1], 2 * m)
        else:
            possible[mode][0] = max(possible[mode][0], row1[i] + row2[i] + 1)
            possible[mode][1] = min(possible[mode][1], row1[i] + row2[i] + m)
    else:
        possible[mode][0] = max(possible[mode][0], row1[i] + row2[i])
        possible[mode][1] = min(possible[mode][1], row1[i] + row2[i])

if possible[0][1] - possible[0][0] < 0 or possible[1][1] - possible[1][0] < 0:
    print(0)
    sys.exit()

for k in range(possible[0][0], possible[0][1] + 1):
    ans[0] += pow(2 * (min(m, k - 1)) - k + 1, zeroes[0], 10 ** 9 + 7)
for k in range(possible[1][0], possible[1][1] + 1):
    ans[1] += pow(2 * (min(m, k - 1)) - k + 1, zeroes[1], 10 ** 9 + 7)

print(ans[0] * ans[1] % (10 ** 9 + 7))
