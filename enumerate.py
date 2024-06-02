# diller = ["Python","js","Flutter"]

# index = 0
# for i in diller:
#     print(f"{index+1}-{diller[index]}")
#     index += 1


# enumerate metod


diller = ["Python","js","Flutter"]

# obje = enumerate(diller)

# print(type(obje))
# print(list(obje))

# for i in enumerate(diller):
#     print(i)

for index,value in enumerate(diller):
    print(f"{index}-{value}")