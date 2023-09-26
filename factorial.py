try:
    a = int(input("Введите число: "))
    total = 1
    
    for i in range(1, a+1):
        total = total * i

    print("Факториал числа", a, "равняется", total)
except:
    print("Некорректный ввод!")