a = 10
b = 20
c = 30

a, b, c = 10, 20, 30

a, b = b, a

a += 5 # => a = a+5
a -= 5 # => a = a+5
a *= 5 # => a = a+5
a /= 5 # => a = a+5
a %= 5 # => a = a+5
a **= 5 # => a = a+5
a //= 5 # => a = a+5


sayilar = (1,2,3,4,5,6)

a,b,*c = sayilar #// c = list

print(a, b, c)
