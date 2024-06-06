class User:
    def __init__(self, username, name, surname, birthday):
        self.username = username
        self.name = name
        self.surname = surname
        self.birthday = birthday
    #instance methods
    def info(self):
        return f"{self.username} kullanici adiyla {self.name} {self.username} sisteme kaydoldu"
    def calculateAge(self):
        return f"{self.username} kullanicisinin yasi : {2024-self.birthday}"

u1 = User("aaa","bbb","cccc",1990)

print(u1.info())
print(u1.calculateAge())