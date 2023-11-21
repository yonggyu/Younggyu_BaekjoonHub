import sys

x = int(sys.stdin.readline())
n = 0
cnt = 0
while n <= x:
    cnt += 1
    n += cnt

print(cnt-1)