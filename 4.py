with open('4задание.txt') as t:
    ty = t.read()
print(sum(map(str.isalpha,ty)))
print(len(ty.split()))
print(len(ty.split('\n')))
