f=open('C:\Users\verag\OneDrive\Документы\КОЛЛЕДЖ\3 курс\МДК 01.01\лр7 файлы списки\7.1задание.txt')  
f1=open('C:\Users\verag\OneDrive\Документы\КОЛЛЕДЖ\3 курс\МДК 01.01\лр7 файлы списки\7задание.txt','a')
b = f.readlines()
    
for word in (b):
    f1.write(word[::-1])


for worda in reversed(b):
    f1.write(worda[::-1])

f.close()
f1.close()