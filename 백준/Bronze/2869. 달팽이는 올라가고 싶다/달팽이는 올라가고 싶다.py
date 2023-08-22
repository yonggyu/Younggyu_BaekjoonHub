a, b, v = map(int, input().split())
temp = int((v - b) / (a - b))

if (v - b) % (a - b) == 0:
    print(temp)
else:
    print(temp + 1)