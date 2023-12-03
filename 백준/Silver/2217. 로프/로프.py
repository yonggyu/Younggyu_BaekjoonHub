import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

result = []

for x in arr:
    result.append(x * n)
    n -= 1

print(max(result))