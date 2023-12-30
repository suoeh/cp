check = set()
for i in range(int(input())):
    snow = list(map(int, input().split()))
    cand = []
    for j in range(6):
        cand += [snow[j:] + snow[:j], snow[j::-1] + snow[:j:-1]]
    cand = tuple(min(cand))
    if cand in check:
        print("Twin snowflakes found.")
        break
    check.add(cand)
else: print("No two snowflakes are alike.")
