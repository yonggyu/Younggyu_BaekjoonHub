cnt = int(input())
arr = []
score = [0] * cnt
temp = 0
tempfor = 1

for i in range(cnt):
  arr.append(list(input()))

for j in range(cnt):
  tempfor = 1
  for k in range(len(arr[j])):
    if arr[j][k] == 'O':
      temp += tempfor
      tempfor += 1
    elif arr[j][k] == 'X':
      tempfor = 1

  score[j] = temp
  temp = 0

for a in range(cnt):
  print(score[a])