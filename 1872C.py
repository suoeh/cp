isPrime = [True for _ in range(10 ** 7 + 1)]
p = 2

while p * p <= 10 ** 7:
    if isPrime[p]:
        for i in range(p * p, 10 ** 7 + 1, p):
            isPrime[i] = False
    p += 1


def solve():
    l, r = map(int, input().split())

    if r < 4:
        return [-1]

    if l != r or l % 2 == 0:
        if l < 3:
            l = 4
        if l % 2 == 0:
            return l // 2, l // 2
        else:
            return (l + 1) // 2, (l + 1) // 2

    if isPrime[l]:
        return [-1]

    for i in range(2, l // 2, 1):
        if (l - i) % i == 0:
            return l - i, i


for _ in range(int(input())):
    print(*solve())
