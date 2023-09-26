try:
    a = input("Введите число: ")
    try:
        int(a)
    except:
        print("Это не число!")
        exit()
    b = input("Введите цифру, которую нужно найти: ")
    if(b.__len__() > 1):
        print("Цифра должна быть одна!")
    else:
        c = a.find(b)
        if(c == -1):
            print("Такой цифры нет!")
        else:
            print("Она есть на позиции №"+str(c+1))
except:
    print("Некорректный ввод!")