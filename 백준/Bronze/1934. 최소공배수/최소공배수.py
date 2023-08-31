x = int(input())

for i in range(x):
    a, b = map(int, input().split())
    temp = a * b
    while b > 0:
        a, b = b, a%b
    temp /= a
    print(int(temp))