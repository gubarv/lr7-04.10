with open('2задание.txt') as datfile:
    f = datfile.read()
print('YES' if input('Введите символ: ') in f else 'NO')

