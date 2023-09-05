import sys

arr = [sys.stdin.readline().rstrip() for i in range(5)]

length = max(len(e) for e in arr)

for j in range(length):
    for k in range(5):
        if j < len(arr[k]):
            print(arr[k][j], end='')