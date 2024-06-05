# True and True => True => All()
# True or False => True => Any()
# sonuc = all([True,False,True])
# sonuc = any([True,False,True])


sayilar = [0,1,4,7,8,10,15]


sonuc = [bool(sayi) for sayi in sayilar]
sonuc = any([bool(sayi) for sayi in sayilar])

sonuc = all([sayi%2 ==0 for sayi in sayilar])

print(sonuc)