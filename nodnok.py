def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return int(a * b / gcd(a, b))

try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))

    import math
    
    nok = lcm(a, b)
    nod = gcd(a, b)

    print("Число 1:", a)
    print("Число 2:", b)
    print("НОК:", nok)
    print("НОД:", nod)
except:
    print("Некорректный ввод!")
