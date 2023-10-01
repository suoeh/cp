from math import lcm

while True:
    n = int(input())
    if n == 0: break
    lst = []
    marked = [False] * n
    count = 0
    loop = []
    ans = 1

    for i in range(n):
        start, end = map(int, input().split())
        lst.append([start, end])

    lst.sort()

    while count != n:
        temp = 1
        ind = marked.index(False)
        marked[ind] = True
        count += 1
        nxt = lst[ind][1] - 1

        while 1:
            if not marked[nxt]:
                temp += 1
                marked[nxt] = True
                count += 1
                nxt = lst[nxt][1] - 1
            else:
                loop.append(temp)
                break

    for i in loop:
        ans = lcm(ans, i)

    print(ans)
