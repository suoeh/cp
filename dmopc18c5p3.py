n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    arr[i] += arr[i - 1]
ans = 0


def check(gap):
    global arr
    for j in range(gap, n + 1):
        if arr[j] - arr[j - gap] < m:
            return True
    return False

l = 1
r = n
while l <= r:
    middle = (l + r) // 2
    if check(middle):
        ans = max(ans, middle)
        l = middle + 1
    else:
        r = middle - 1
print(ans)
