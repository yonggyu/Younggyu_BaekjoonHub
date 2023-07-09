count = int(input())
num = list(map(int, input().split()))
v = int(input())
temp = 0

for i in range(count):
    if num[i] == v:
        temp += 1

print(temp)