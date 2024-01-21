import sys

input = sys.stdin.readline


# MOD = 10 ** 9 + 7
def mergeArr(arr):
    newarr = []
    add = [arr[0][0], arr[0][1]]
    for i in range(len(arr) - 1):
        if arr[i][1] >= arr[i + 1][0]:
            add[1] = arr[i + 1][1]
        else:
            newarr.append(add)
            add = [arr[i + 1][0], arr[i + 1][1]]
    newarr.append(add)
    return newarr


def clearArr(arr, left, right):
    newarr = []
    for i in range(len(arr)):
        values = [inBounds(arr[i][0], left, right), inBounds(arr[i][1], left, right)]
        if values[0] and values[1]:
            continue
        elif values[0] and not values[1]:
            newarr.append([right + 1, arr[i][1]])
        elif not values[0] and values[1]:
            newarr.append([arr[i][0], left - 1])
        elif arr[i][1] > right and arr[i][0] < left:
            newarr.append([arr[i][0], left - 1])
            newarr.append([right + 1, arr[i][1]])
        else:
            newarr.append([arr[i][0], arr[i][1]])
    return newarr


def inBounds(n, left, right):
    if left <= n <= right: return True
    return False


def solve():
    n, m, k = map(int, input().split())
    time = 0
    valid = [[0, 0]]
    for i in range(m):
        a, b, t = map(int, input().split())
        delta = t - time
        time = t

        for j in range(len(valid)):
            valid[j][0] = max(0, valid[j][0] - k * delta)
            valid[j][1] = min(n, valid[j][1] + k * delta)
        valid = mergeArr(valid)
        print(valid, "merged")
        valid = clearArr(valid, a, b)
        print(valid, "cleared")
        if not valid: return "NO"

    return "YES"


print(solve())
