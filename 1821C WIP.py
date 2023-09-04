def check(s1, s2):
    l1, l2 = set(), set()

    for i in s1:
        l1.add(i)

    for i in s2:
        l2.add(i)

    return len(l1), len(l2)


def spl(n):
    n = [[n[i] for i in range(0, len(n), 2)], [n[i] for i in range(1, len(n), 2)]]
    return n[0], n[1]


def solve():
    t = [*input()]
    moves = 0
    c = True

    s1, s2 = spl(t)

    for i in t:
        if i != t[0]:
            c = False
            break

    if c: return moves

    while 1:
        moves += 1
        v1, v2 = check(s1, s2)

        if v1 == 1 or v2 == 1:
            return moves

        if v1 <= v2:
            t = s1
            s1, s2 = spl(t)
        else:
            t = s2
            s1, s2 = spl(t)


for _ in range(int(input())):
    print(solve())
