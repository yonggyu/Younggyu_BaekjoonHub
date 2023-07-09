temp = int(input())
num = temp
cycle = 0

def func1():
    global num, cycle
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c
    cycle += 1

    if num == temp:
      print(cycle)
      return
    else:
      func1()

func1()