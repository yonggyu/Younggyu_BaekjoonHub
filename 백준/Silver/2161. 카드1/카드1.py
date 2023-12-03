import sys

x = int(sys.stdin.readline())

arr = [i for i in range(1, x+1)]
trash = []

while len(arr) > 1:
    trash.append(arr.pop(0))
    arr.append(arr.pop(0))

result = trash + arr

for n in result:
    print(n, end=' ')