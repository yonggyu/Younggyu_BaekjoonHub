x = list(map(int, input().split()))

for i in range(7):
    if x[i+1] - x[i] == 1:
        temp = "ascending"
    elif x[i+1] - x[i] == -1:
        temp = "descending"
    else:
        temp = "mixed"
        break

print(temp)
