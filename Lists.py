from Card import Card

class Random(): pass

class Lists:

    def __init__(self,Id):
        self.Id = Id
        self.name = ""
        self.description = ""
        self.cards={}



    def createCard(self,cardName):
        cardId = str(id(Random()))
        c = Card(cardId)
        c.setName(cardName)
        self.cards[cardId] = c
        return cardId


    def deleteCard(self,cardId):
        del self.cards[cardId]



    def setName(self,name):
        self.name = name


    def setDescription(self,desc):
        self.description = desc


    def issCard(self,cardId) -> bool:       #return true for a card
        if cardId in self.cards: return True
        return False




    def displayList(self):
        print("\tList ID:",self.Id,"\nNAME",self.name)
        if self.cards:
            for i in self.cards:
                self.cards[i].displayCards()