# key - value

# plakalar = {"Izmir": 35, "Istanbul": 34}

# print(plakalar["Izmir"])

# plakalar["Eskisehir"] = 26

# print(plakalar)


urunler = {
    100: { 
        "urunAdi" : "Monitor",
        "urunAciklamasi" : "16",
        "garantiSuresi" : 3,
        "fiyati" : [800,944],
    },
    101 : 
    { 
        "urunAdi" : "SSD",
        "urunAciklamasi" : "256 GB",
        "garantiSuresi" : 2,
        "fiyati" : 500
    }
}

sonuc = urunler[100]["fiyati"]
tutar = urunler[100]["fiyati"][1] + urunler[101]["fiyati"]

print(tutar)