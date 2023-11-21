import sys

x = int(sys.stdin.readline())
arr = [0]*x
for i in range(x):
    arr[i] = list(map(int, sys.stdin.readline().split()))

arr.sort()

for i in range(0, len(arr)):
    for x in arr[i]:
        print(x, end=' ')
    print()