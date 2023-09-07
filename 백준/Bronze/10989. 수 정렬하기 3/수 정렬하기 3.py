import sys

x = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(x):
    temp = int(sys.stdin.readline())
    arr[temp] += 1

for j in range(10001):
    if arr[j] != 0:
        for k in range(arr[j]):
            print(j)
