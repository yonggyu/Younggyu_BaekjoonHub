i = 0
score = []

while True:
    num = int(input())
    if num == 0:
        break
    num_list = list(map(int, str(num)))
    num_list_Rev = num_list[::-1]

    if num_list == num_list_Rev:
        score.append(1)
        i += 1
    else:
        score.append(0)
        i += 1

cnt = len(score)

for j in range(cnt):
    if(score[j] == 1):
        print("yes")
    else:
        print("no")
