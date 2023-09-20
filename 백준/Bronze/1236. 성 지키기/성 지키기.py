import sys

x, y = map(int, input().split())
temp = []

for i in range(x):
    row = sys.stdin.readline().strip()
    temp.append(row)

row = 0
col = 0

for i in range(x):
    if 'X' not in temp[i]:
        row += 1

for j in range(y):
    if 'X' not in [temp[k][j] for k in range(x)]:
        col += 1

print(max(row, col))