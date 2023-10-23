word = input().upper()
set_word = list(set(word))
cnt = []

for x in set_word:
    cnt.append(word.count(x))

if cnt.count(max(cnt)) > 1:
    print("?")

else:
    print(set_word[cnt.index(max(cnt))])