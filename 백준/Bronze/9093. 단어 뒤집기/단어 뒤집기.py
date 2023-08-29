x = int(input())

for i in range(x):
    temp = input().split()
    for j in temp:
        print(j[::-1], end=' ')