action = input("Введите от 'а' до 'д': ").lower() #а б в г д
 
with open('5задание.txt') as f:
    data = f.readlines()
if action == 'а':
    print(*data[0])
elif action == 'б':
    print(*data[4])
elif action == 'в':
    print(*data[0:4])
elif action == 'г':
    s1, s2 = map(int, input('Введите s1 и s2 через пробел: ').split())
    print(*data[s1-1 : s2-1])
elif action == 'д':
    print(*data)
    
