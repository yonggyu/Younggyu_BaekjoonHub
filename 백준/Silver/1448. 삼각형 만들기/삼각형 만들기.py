import sys

x = int(sys.stdin.readline())

arr = []
result = -1

for _ in range(x):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)

for i in range(x - 2):
    if arr[i] < arr[i + 1] + arr[i + 2]:
        result = arr[i] + arr[i + 1] + arr[i + 2]
        break

print(result)