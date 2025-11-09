import random

def hileli_zar(n):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0

    for i in range(n):
        x = random.randint(1,6)

        if x == 1:
            a += 1
        elif x == 2:
            b += 1
        elif x == 3:
            c += 1
        elif x == 4:
            d += 1
        elif x == 5:
            e += 1
        else:
            f += 1

        # s'yi her adımda hesapla
        s = a + b + c + d + e + f

        # oranları yazdır
        print("a sayısı:", a / s)
        print("b sayısı:", b / s)
        print("c sayısı:", c / s)
        print("d sayısı:", d / s)
        print("e sayısı:", e / s)
        print("f sayısı:", f / s)
        print("------") 

hileli_zar(36)