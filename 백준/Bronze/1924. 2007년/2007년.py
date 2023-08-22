x, y = map(int, input().split())

days = y

for i in range(1, x):
    if i == 2:
        days += 28
    elif i in [4, 6, 9, 11]:
        days += 30
    else:
        days += 31

days %= 7

if days == 1:
    result = "MON"
elif days == 2:
    result = "TUE"
elif days == 3:
    result = "WED"
elif days == 4:
    result = "THU"
elif days == 5:
    result = "FRI"
elif days == 6:
    result = "SAT"
else:
    result = "SUN"

print(result)