abc = input()
abc = abc.split('.')
result = ''

for x in abc:
    n = len(x)
    if n % 2 != 0:
        print('-1')
        exit(0)
    else:
        result += 'A' * (n // 4 * 4)
        n = n % 4
        result += 'B' * (n // 2 * 2)
    result += '.'

result = result[:-1]
print(result)
