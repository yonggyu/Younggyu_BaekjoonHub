cnt = int(input())
ary = list(map(int, input().split()))
M = max(ary)

for j in range(cnt):
  ary[j] = ary[j] / M * 100

result = sum(ary) / cnt

print(result)