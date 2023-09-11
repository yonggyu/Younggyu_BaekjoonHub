import sys

x = int(sys.stdin.readline())
arr = []

for i in range(x):
    arr.append(list(sys.stdin.readline().split()))

arr.sort(key=lambda a:int(a[0]))

for j in arr:
    print(j[0], j[1])