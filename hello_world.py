import random

while True:
    zar1=random.randint(1, 6)
    zar2=random.randint(1,6)
    toplam = zar1+zar2
    count =3
   
    if (zar1+zar2)>= 8:
        count -=1
        print(f"Oyunu kazandız,toplma sayınız: {toplam}")
        break
    elif   (zar1+zar2)== 6 or (zar1+zar2)== 7:
        count-=1
        print("Zarları tekrar atınız!!!")
    else:
        print("Oyunu kaybettiniz.Daha sonra tekrar deneyiniz")  
        break 
