import random

def MC(n):
    A=0
    B=0
    for i in range(n):
        x=10*random.randint(0,10)
        y=10*random.randint(0,10)
        if (x**2+y**2)<1:
            B+=1
        elif (x**2+y**2)<9 and (x**2+y**2)>4:
            A+=1

    print("sonuc:", A, "adet A bölgesinde,", B, "adet B bölgesinde nokta var.")