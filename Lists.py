from Card import Card

import Random

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
        cards[cardId] = c
        return cardId


    def deleteCard(self,cardId):
        del cards[cardId]



    def setName(self,name):
        self.name = name


    def setDescription(self,desc):
        self.description = desc


    def issCard(self,cardId) -> bool:       #return true for a card
        if cardId in cards: return True
        return False




    def displayList(self):
        print("List ID:",self.id,"/nNAME",self.name,"/nCARDS:")
        for i in cards:
            print("/n",i,"/n")
            i.displayCards()