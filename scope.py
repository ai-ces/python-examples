#global scope

# a = " global deger"



# def fn1():
#     #local scope
#     a = "local deger"
#     print(a)

# fn1()
# print(a)


#---------------------------------------------

a = 10

def fn2():

    global a 
    #print(f"a: {a}")

    a = 20
    print(f"changed a to {a}")

fn2()
print(a)