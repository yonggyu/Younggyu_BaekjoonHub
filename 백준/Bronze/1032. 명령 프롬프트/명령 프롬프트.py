import sys

x = int(sys.stdin.readline())

temp = list(sys.stdin.readline())

for _ in range(x-1):
    temp2 = list(sys.stdin.readline())
    for i in range(len(temp)):
        if temp[i] != temp2[i]:
            temp[i] = "?"

print(''.join(temp))