# Ввод пользователя
a = input("Введите числа через запятую: ")

# Форматируем числа
a = a.split(",") # создаём массив из строки
for i in range(a.__len__()):
    try:
        a[i] = int(a[i])
    except:
        del a[i]

# Выводим min и max
print("Массив:", a)
print("Минимальное:", min(a))
print("Максимальное:", max(a))