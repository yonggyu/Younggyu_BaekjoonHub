x = int(input())
temp = 0

while True:
    if x % 5 == 0:
        temp += x // 5
        break
    else:
        x -= 3
        temp += 1
    if x < 0:
        temp = -1
        break

print(temp)