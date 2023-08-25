num = int(input())
arr = list(map(int, input().split()))
sum = 0
result = 0

arr.sort()

for i in range(num):
    sum += arr[i]
    result += sum

print(result)