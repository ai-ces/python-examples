# isim = ""

# for harf in isim:
#     if (harf == ""):
#         break
#     print(harf)



# i = 0

# while (i < 10):
#     i += 1
#     if (i == 5):
#         continue
#     print(i)


# 1-100 arasindaki tek sayilarin toplami

i = 0
toplam = 0

while (i<=100):
    i += 1
    if (i % 2 == 0):
        continue
    toplam += i
print(f'toplam: {toplam}')