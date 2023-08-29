x = int(input())

a, b = 0, 1

for i in range(x):
    a, b = b, a + b

print(a)