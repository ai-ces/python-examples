list1 = [1,3,5,13]

thistuple = (1,2, False)
thistuple2 = (1,2,5,6, False)

print(type(list1))
print(type(thistuple))

print(list1[0])
print(thistuple[2])

print(len(list1))
print(len(thistuple))

# tuples can not be changed
# list1[0] = 6
# thistuple[0] = 7

# print(list1)
# print(thistuple)

print(list1.count(3))
print(thistuple.count(2))

print(list1)
print(thistuple)

print(thistuple + thistuple2)

