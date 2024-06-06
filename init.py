
class Product:
    def __init__(self, name, price,isActive):
        self.name = name
        self.price = price
        self.isActive = isActive
        print("product nesnesi olusturuldu")


p1 = Product("Mercedes A","70000000",True)
p2 = Product("BMW","50000000",False)


print(p1.name,p1.price,p1.isActive)
print(p2.name,p1.price,p2.isActive)