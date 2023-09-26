try:
    a = int(input("Введите основание степени: "))
    b = int(input("Введите показатель степени: "))

    total = a
    
    for i in range(1, b):
        total = total * a
    
    if(b == 0):
        total = 1
    if(total == 0):
        total = "степень не определена"
    print("Результат:", total)
except:
    print("Некорректный ввод!")