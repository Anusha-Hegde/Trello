from User import User

class Card:

    def __init__(self,Id):
        self.name = ""
        self.Id = Id
        self.description = ""
        self.user=None


    def setName(self,name):
        self.name = name


    def setDescription(self,desc):
        self.description = desc


    def isAssUser(self) -> bool:
        if not self.user:
            return False  
        return True

    def assUser(self,userId):
        if not self.user:
            self.user = User(userId)
            return
        print("user for the card already assigned")

    def unAssUser(self):
        if not self.user:
            print("no user assigned to the card")
            return
        self.user = None


    def displayCards(self):
        print("\t\tCard ID:",self.Id,"\tNAME:",self.name,"\tDescription:",self.description)
        if self.isAssUser():
            self.user.displayUser()