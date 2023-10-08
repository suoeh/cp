import sys

read = sys.stdin.readline


def solve():
    n = int(read())
    value = 0
    score = 0
    scores = []
    cand = dict()

    for _ in range(n):
        p, w, d = map(int, read().split())
        score += w * max(abs(p) - d, 0)

        if (p + d) not in cand:
            cand[p + d] = w
        else:
            cand[p + d] += w

        if (p - d) > 0:
            value -= w
            if (p - d) not in cand:
                cand[p - d] = w
            else:
                cand[p - d] += w

    candList = list(zip(cand.keys(), cand.values()))
    candList.sort()
    slider = 0

    for index, update in candList:
        score += value * (index - slider)
        value += update
        slider = index
        scores.append(score)

    return min(scores)


print(solve())
