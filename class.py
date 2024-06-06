# Class

class Arac:
    pass



# Instance, object


arac1 = Arac()
arac2 = Arac()

print(type(Arac))
print(arac1,arac2)



class Products:
    pass


p1 = Products()
p2 = Products()
p3 = Products()

listProduct = [p1,p2,p3]

for p in listProduct:
    print(p)
    print(type(p))