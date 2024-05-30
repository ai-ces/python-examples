
carAudi = {
    "marka" : "Audi",
    "model" : "A5",
    "yil" : 2019,
}

# sonuc = carAudi["marka"]
# sonuc = carAudi.get("marka")

sonuc = "marka" in carAudi

sonuc = len(carAudi)

# add

carAudi["renk"] = "siyah"

#delete

carAudi.pop("yil")

# after python 3.7
carAudi.popitem()

del carAudi["marka"]


# for delete object
del carAudi


carAudi.clear()


#copy

car = carAudi.copy()

print(car)

#update

carAudi.update({
    "marka" : "BMW",
    "renk"  : "beyaz"
})

print(sonuc)