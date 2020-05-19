import User

class Card:

    def __init__(self,Id):
        self.name = ""
        self.Id = Id
        self.user=None


    def setName(self,name):
        self.name = name

    def isAssUser(self) -> bool:
        if self.user is None:
            return False  
        return True

    def assUser(self,userId):
        self.user = User(userId)

    def unAssUser(self):
        self.user = None


    def displayCards(self):
        print("\t\tCard ID:",self.Id,"/nNAME",self.name,"/n")
        if isAssUser:
            user.displayUser()


            