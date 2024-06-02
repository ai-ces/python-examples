# sayilar = []

# for  i in range(10):
#      sayilar.append(i)
# print(sayilar)


sayilar = [i for i in range(10)]
sayilar = [i*2 for i in range(10)]
sayilar = [i*i for i in range(10)]

liste = [3,8,5,12,40]

sayilar = [i*2 for i in liste]
sonuc = [str(sayi) for sayi in liste]

print(sonuc)