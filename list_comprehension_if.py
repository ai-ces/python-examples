
sayilar = [1,3,12,22,34]
sonuc = []

for sayi in sayilar:
    if (sayi % 2 == 0):
        sonuc.append(sayi)



sonuc = [sayi for sayi in sayilar if sayi % 2 == 0]
sonuc = [sayi if sayi % 2==1 else "cift sayi" for sayi in sayilar]

print(sonuc)

