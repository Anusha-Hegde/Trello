class User:

    def __init__(self,Id):
        self.Id = Id
        self.name = ""
        self.__email = ""

    def displayUser(self):
        print("\t\t\tUserId:"+self.Id)

    