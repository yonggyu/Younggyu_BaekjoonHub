cnt = int(input())
num = []

for i in range(cnt):
    num.append(int(input()))

for j in range(cnt):
  min = j
  for k in range(j+1, cnt):
    if num[k] < num[min]:
      num[k], num[min] = num[min], num[k]
for a in range(cnt):
  print(num[a])