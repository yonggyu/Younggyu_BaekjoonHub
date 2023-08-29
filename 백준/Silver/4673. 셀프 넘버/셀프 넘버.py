arr = set()

def d(n):
    n += sum(map(int, str(n)))
    return n

for i in range(1, 10001):
    arr.add(d(i))

for j in range(1, 10001):
    if j not in arr:
        print(j)