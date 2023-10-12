x = int(input())
groupCheck = 0

for _ in range(x):
    word = input()

    for i in range(len(word) - 1):
        if word[i] != word[i+1]:
            group = word[i+1:]
            if word[i] in group:
                groupCheck -= 1
                break

    groupCheck += 1

print(groupCheck)