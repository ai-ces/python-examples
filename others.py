# Identity Operator : is

x = y = [1,2,3,4]

z = [1,2,3,4]

print(x==y) # true
print(x==z) #true

print(x is z) # false
print(x is y) # true


# membership

a = ["python", "js"]

print("python" in a)

email = ""
 
print("@" in email)