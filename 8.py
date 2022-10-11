count = 0
eq = True
with open("C:\Users\verag\OneDrive\Документы\КОЛЛЕДЖ\3 курс\МДК 01.01\лр7 файлы списки\8задание.txt", "r", encoding = "utf-8") as f1, open("C:\Users\verag\OneDrive\Документы\КОЛЛЕДЖ\3 курс\МДК 01.01\лр7 файлы списки\8.1задание.txt", "r", encoding = "utf-8") as f2:
    for a1, a2 in zip(f1, f2):
        count += 1
        if a1 != a2:
            eq = False
            break

if eq == True:
    print("Нет отличий")
else:
    print("Отличается строка ", count)