import math

T = int(input())

for i in range(T):
    N, M = map(int, input().split())

    if N <= M:
        temp = M
        M = N
        N = temp

    print(math.comb(N, M))