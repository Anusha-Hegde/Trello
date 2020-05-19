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
        self.user = User(userId)

    def unAssUser(self):
        self.user = None


    def displayCards(self):
        print("\t\tCard ID:",self.Id,"\tNAME",self.name)
        if self.isAssUser():
            self.user.displayUser()