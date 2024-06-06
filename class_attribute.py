class User:

    active_user = 0

    def __init__(self,username,name,surname,age):

        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        User.active_user += 1

    def userName(self):
        return f"{self.username}"
    
    def logout(self):
        User.active_user -= 1
        return f"{self.username} programdan cikis yapti"

print(f"Aktif kullanici sayisi :{User.active_user}")
user1 = User("aaa","bbb","ccc",39)
user2 = User("ddd","eee","ffff",37)        
user3 = User("ggg","hhh","jjjj",40)

print(f"Aktif kullanici sayisi :{User.active_user}")