from User import User

class Card:

    def __init__(self,Id):
        self.name = ""
        self.Id = Id
        self.user=None


    def setName(self,name):
        self.name = name

    def isAssUser(self) -> bool:
        if not self.user:
            return False  
        return True

    def assUser(self,userId):
        if not self.user:
            self.user = User(userId)
            return
        print("user exists")

    def unAssUser(self):
        if not self.user:
            print("user not exists")
            return
        self.user = None


    def displayCards(self):
        print("\t\tCard ID:",self.Id,"\tNAME",self.name)
        if self.isAssUser():
            self.user.displayUser()