x = int(input())

row = 1

while x > row:
    x -= row
    row += 1

if row % 2 == 0:
    up = x
    down = row - x + 1

else:
    up = row - x + 1
    down = x

print(up, '/', down, sep="")