r, c = map(int, input().split())
rows = list(map(int, input().split()))
columns = list(map(int, input().split()))
col = 0
rowSet = {}
columnSet = {}

for i in range(r):
    if rows[i] != -1:
        if rows[i] - i not in rowSet:
            rowSet[rows[i] - i] = 0
        rowSet[rows[i] - i] += 1

for i in range(c):
    if columns[i] != -1:
        if columns[i] - i not in columnSet:
            columnSet[columns[i] - i] = 0
        columnSet[columns[i] - i] += 1

for i in rowSet:
    if i in columnSet:
        col += min(rowSet[i], columnSet[i])

print(col)
