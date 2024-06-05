
# sayilar = [1,3,5,8,12]

# kareleri = []

# for sayi in sayilar:
#     kareleri.append(sayi ** 2)

# print(kareleri)

sayilar = [1,3,5,8,12]
str_sayilar = ["1","3","5","8","12"]

def kareAl(sayi):
    return sayi ** 2
sonuc = list(map(kareAl, sayilar))
sonuc = list(map(lambda sayi: sayi ** 2, sayilar))
sonuc = list(map(int, str_sayilar))

print(sonuc)