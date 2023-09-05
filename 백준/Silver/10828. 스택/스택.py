import sys

n = int(sys.stdin.readline())
stack = []
top = -1

for i in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        stack.append(cmd[1])
        top += 1
    elif cmd[0] == "pop":
        if top == -1:
            print(-1)
        else:
            print(stack.pop())
            top -= 1
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        if top == -1:
            print(1)
        else:
            print(0)
    elif cmd[0] == "top":
        if top == -1:
            print(-1)
        else:
            print(stack[top])