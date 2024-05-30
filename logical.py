# And

 x = 15 # true
 x = 25 # false

sonuc = 10 < x < 20


sonuc = (x > 10) and (x < 20)

# True and True => True 
# True and False => False
# False and False => False


karne_notu = 60
devamsizlik = 6

sonuc = (karne_notu => 50) and (devamsizlik < 10) 



# OR

# True or True => True 
# True or False => True
# False or False => False


sonuc = (x < 10) or (x % 3 == 0) # true or false = true



# not

sonuc = not(x > 0) # true to false, false to true

ceza_bilgisi = False
sonuc = (karne_notu >= 85) and (devamsizlik < 10) and (ceza_bilgisi = false)

print(sonuc)
