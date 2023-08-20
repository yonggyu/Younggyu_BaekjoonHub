x = list(map(int, input().split()))

def factorial(num):
    temp = 1
    for i in range(1, num + 1):
        temp *= i
    return temp

result = factorial(x[0]) // (factorial(x[1]) * factorial(x[0] - x[1]))
print(result)