wordlist = []
f = open("C:\Users\verag\OneDrive\Документы\КОЛЛЕДЖ\3 курс\МДК 01.01\лр7 файлы списки\6задание.txt",'r')
for word in f.readlines():
    wordlist.append(word.strip())

# Ищем номер самой длинной строки
dl = 0
number = 0
length = 0
for i in range(len(wordlist)):
    if len(wordlist[i]) > length:
        length = len(wordlist[i])
        dl = len(wordlist[i])
        line = wordlist[i]
        number = i
f. close()        
print("а) " + str(number),"б) " + str(dl),"в) " +  line, sep="\n")