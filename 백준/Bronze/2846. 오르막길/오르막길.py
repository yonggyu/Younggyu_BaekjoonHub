import sys

x = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
temp = []
ascend = 0

for i in range(x-1):
    if arr[i] < arr[i+1]:
        ascend += arr[i+1] - arr[i]
        temp.append(ascend)
    else:
        temp.append(ascend)
        ascend = 0

print(max(temp))