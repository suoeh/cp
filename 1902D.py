import sys

input = sys.stdin.readline

m, q = map(int, input().split())
moves = input()
translate = {"R": 0, "L": 1, "U": 2, "D": 3}
coord = {(0, 0): [1]}

location = [0, 0]
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # R L U D
memo = [(0, 0)] + [0] * m


def rotate(x1, y1, xp, yp):
    return 2 * xp - x1, 2 * yp - y1


for i in range(m):
    location[0] += move[translate[moves[i]]][0]
    location[1] += move[translate[moves[i]]][1]
    if (location[0], location[1]) in coord.keys():
        coord[(location[0], location[1])].append(i + 2)
    else:
        coord[(location[0], location[1])] = [i + 2]
    memo[i + 1] = (location[0], location[1])


def solve():
    x, y, l, r = map(int, input().split())
    # find if point on coord has key out of range
    if (x, y) in coord.keys():
        # print(coord[(x, y)])
        if coord[(x, y)][0] <= l or coord[(x, y)][-1] > r:
            return "YES"

    # flip, find new point with key in range
    nx, ny = rotate(x, y, (memo[r][0] + memo[l - 1][0]) / 2, (memo[r][1] + memo[l - 1][1]) / 2)

    # print(nx, ny)

    if (nx, ny) in coord.keys():
        # print(coord[(nx, ny)])
        for _ in coord[(nx, ny)]:
            if l <= _ <= r:
                return "YES"

    return "NO"


for _ in range(q):
    print(solve())
