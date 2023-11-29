import sys

x = int(sys.stdin.readline())

arr = []

for _ in range(x):
    arr.append(int(sys.stdin.readline()))

arr.sort()

avg = round(sum(arr) / len(arr))
print(avg)

mean = arr[len(arr) // 2]
print(mean)

count = {}
for x in arr:
    if x not in count:
        count[x] = 0
    count[x] += 1

max_value = max(count.values())
mode = [k for k, v in count.items() if v == max_value]

if len(mode) > 1:
    print(mode[1])
else:
    print(mode[0])

print(max(arr)-min(arr))