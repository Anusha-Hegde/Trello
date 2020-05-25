from Lists import Lists 
from User import User

class Random(): pass 

class Board():
    def __init__(self,id):
        self.id = id  
        self.name = ""
        self.privacy = "public"
        self.url = "trello.com/"+id     
        self.list={}
        self.members=[]



    def setPrivacy(self,privacy):
        '''
        sets board's privacy
        params:
            privacy(str): new privacy
        returns: 
            None
        '''        
        self.privacy = privacy


    def setName(self,name):
        self.name = name


    
    def createList(self,listName):
        '''
        
        '''
        listId = str(id(Random()))
        l = Lists(listId)
        l.setName(listName)
        self.list[listId] = l
        return listId


    def isList(self,listId) -> bool:    #check if list exists
        if listId in self.list: return True


    def isCard(self,cardId):    #check if card exists and return listID
        for i in self.list: 
            if self.list[i].issCard(cardId): return i
        return -1


    def deleteList(self,listId):
        if listId in self.list:
            del self.list[listId]



    def addMember(self,userId):
        self.members.append(User(userId))

    
    def removeMember(self,userId):
        for i in self.members:
            if userId == i.Id:
                self.members.remove(i)
                return
        print("not a member")


    def displayBoard(self):
        print("Board ID:",self.id,"\tNAME:",self.name,"\tURL:",self.url,"\tPrivacy:",self.privacy,"\tMembers:\n")
        if self.members:
            for i in self.members:
                i.displayUser()
        if self.list:
            for i in self.list:
                self.list[i].displayList()
