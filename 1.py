with open('1задание.txt') as datfile:
    text = datfile.read()
print(sum(map(int, text.split(None, 2)[:2])))