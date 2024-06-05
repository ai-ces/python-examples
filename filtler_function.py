
yaslar = [7,15,18,27,36]

def yetiskinmi(x):
    if x<18:
        return False
    else:
        return True

sonuc = list(filter(yetiskinmi,yaslar))
sonuc = list(filter(lambda x: x>=18, yaslar))


print(sonuc)