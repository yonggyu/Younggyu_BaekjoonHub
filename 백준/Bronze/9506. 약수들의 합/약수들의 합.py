while True:
    x = int(input())
    result = []
    temp = 0

    if x == -1:
        break

    for i in range(1, x):
        if x % i == 0:
            result.append(i)
            temp += i

    if sum(result) == x:
        print(x, " = ", " + " .join(str(i) for i in result), sep="")
    else:
        print(x, "is NOT perfect.")