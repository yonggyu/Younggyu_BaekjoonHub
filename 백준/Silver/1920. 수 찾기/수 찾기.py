x1 = int(input())
x1Num = list(map(int, input().split()))
x1Num.sort()

x2 = int(input())
x2Num = list(map(int, input().split()))

def binary_search(array, target):
    start = 0
    end = len(array) - 1
    search = False

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            print(1)
            search = True
            break
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1

    if not search:
        print(0)

for i in range(x2):
    binary_search(x1Num, x2Num[i])