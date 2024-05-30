sayi = -5

if (sayi < 0):

    print("Sayi negatiftir")
else:
    print("Sayi pozitiftir")


giris = True

if (giris):
    print("Merhaba")
else:
    print("Tekrar deneyiniz")


username = ""
passowrd = ""


if (username == "") and (password == ""):
    print("Sisteme giris yaptiniz")
else:
    print("Girilen bilgiler hatalidir")



    if (username == ""):
        if (passowrd == ""):
            print("Sisteme giris yaptiniz")
        else:
            print("Parola hatali")
    else:
        print("Kullanici adiniz yanlis")