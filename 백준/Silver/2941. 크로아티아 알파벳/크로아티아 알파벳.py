arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
result = len(word)

for i in range(len(word)):
    if len(word) < 2:
        result = len(word)
    elif len(word) == 2:
        if word[i-2] + word[i-1] in arr:
            result = 1
    elif word[i-3] + word[i-2] + word[i-1] in arr:
        result -= 2
    elif word[i-2] + word[i-1] in arr:
        result -= 1

print(result)