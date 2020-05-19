from Lists import Lists 
from User import User

class Random(): pass 

class Board():
    def __init__(self,id):
        self.id = id  
        self.name = ""
        self.privacy = "PUBLIC"
        self.url = ""
        self.list={}
        self.members=[]



    def setPrivacy(self,privacy):
        self.privacy = privacy


    def setName(self,name):
        self.name = name


    
    def createList(self,listName):
        listId = str(id(Random()))
        l = Lists(listId)
        l.setName(listName)
        self.list[listId] = l
        return listId


    def isList(self,listId) -> bool:    #check if list exists
        if listId in self.list: return True


    def isCard(self,cardId) :    #check if card exists and return listID
        for i in list: 
            if list[i].issCard(cardId): return i
        return -1


    def deleteList(self,listId):
        if listId in list:
            del list[listId]



    def addMember(self,userId):
        self.members.append(User(userId))

    
    def removeMember(self,userId):
        if User(userId) in self.members:
            self.members.remove(User(userId))
        else: print("not a member")


    def displayBoard(self):
        print("Board ID:",self.id,"\tNAME:",self.name,"\tURL",self.url,"\tLIST:\n")
        if list:
            for i in self.list:
                print("/n",i,"/n")
                list[i].displayList()
