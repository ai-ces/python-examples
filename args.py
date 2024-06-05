# numbers = [5,15,20,25]

# def topla(a,b):
#     return a + b

# def topla(a,b,c):
#     return a + b + c

# def topla(sayilar):
#     sonuc = 0
#     for i in sayilar:
#         sonuc += i
#     return f"Sayilarin  toplami: {sonuc}"

# print(topla(numbers))

 #// * = sinirsiz degisken 

def topla(*args):
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc

print(topla(5,15,25))
print(topla(25.25,25,35,45))