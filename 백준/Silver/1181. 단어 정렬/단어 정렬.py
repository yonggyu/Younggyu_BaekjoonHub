import sys

n = int(sys.stdin.readline())
ary = []

for i in range(n):
    ary.append(sys.stdin.readline().strip())
set_ary = set(ary)
ary = list(set_ary)
ary.sort()
ary.sort(key = len)

for i in ary:
    print(i)