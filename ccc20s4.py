def calc(k):
    return k[0][0] + k[0][1] + max(k[1][1], k[2][1])


n = list(input())
c = [n.count("A"), n.count("B"), n.count("C")]
psa = [[0, 0], [0, 0], [0, 0]]
n = n + n
ans = 9999999

if n[0] == 'A':
    psa[0][1] += 1
elif n[0] == 'B':
    psa[1][1] += 1
else:
    psa[2][1] += 1

for i in range(1, len(n)):
    psa[0].append(psa[0][-1])
    psa[1].append(psa[1][-1])
    psa[2].append(psa[2][-1])

    if n[i] == 'A':
        psa[0][-1] += 1
    elif n[i] == 'B':
        psa[1][-1] += 1
    else:
        psa[2][-1] += 1

for i in range(len(n) // 2):
    miss = [[psa[1][i + c[0]] - psa[1][i], psa[2][i + c[0]] - psa[2][i]],
            [psa[0][i + c[0] + c[1]] - psa[0][i + c[0]], psa[2][i + c[0] + c[1]] - psa[2][i + c[0]]],
            [psa[0][i + c[0] + c[1] + c[2]] - psa[0][i + c[0] + c[1]],
             psa[1][i + c[0] + c[1] + c[2]] - psa[1][i + c[0] + c[1]]]]
    ans = min(ans, calc(miss))
    miss = [[psa[1][i + c[0]] - psa[1][i], psa[2][i + c[0]] - psa[2][i]],
            [psa[0][i + c[0] + c[2]] - psa[0][i + c[0]], psa[1][i + c[0] + c[2]] - psa[1][i + c[0]]],
            [psa[0][i + c[0] + c[2] + c[1]] - psa[0][i + c[0] + c[2]],
             psa[2][i + c[0] + c[2] + c[1]] - psa[2][i + c[0] + c[2]]]]
    ans = min(ans, calc(miss))

print(ans)
