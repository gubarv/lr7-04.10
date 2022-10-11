with open('3задание.txt') as t:
    print(*(sum(map(int, line.split())) for line in t.readlines()), sep='\n')
