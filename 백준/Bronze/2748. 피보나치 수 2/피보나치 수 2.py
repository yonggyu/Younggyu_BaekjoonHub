import sys

x = int(sys.stdin.readline())

result = 1
temp = 0
if x < 1:
    result = temp
elif x == 1:
    pass
elif x >= 2:
    for i in range(2, x+1):
        a = result
        result = temp + result
        temp = a

print(result)