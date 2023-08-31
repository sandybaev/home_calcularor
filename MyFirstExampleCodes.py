import math

PI = math.pi
def radius():
    n = float(input("Введите диаметр в см: "))
    n /= 2
    return n

def height():
    m = float(input("Введите высоту в см: "))
    return m

def volume():
    r = radius()
    h = height()
    s = PI*r**2
    v = s*h

    return v

print("Объем цилиндра:", volume(), " см3")
