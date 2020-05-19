from Board import Board
from itertools import count


class Random(): pass

print("Enter commands\n")
boards={}   #dictionary of board id's and objects

def createBoard(bName):
    Id = str(id(Random()))
    b = Board(Id)
    b.setName(bName)
    boards[Id] = b
    return Id 

def main():
   
    while(1):
        inp = input().split(' ')


        if inp[0] == "BOARD":

            if inp[1] == "CREATE":
                print("board created successfully = ",createBoard(inp[2]))
                

            elif inp[1] == "DELETE":
                key = int(inp[2])
                if key in boards:
                    del boards[key] 
                else:
                    print("board not found")
                

            elif inp[2] == "name":
                boards[inp[1]].setName(inp[3])
                print("name changed to",inp[3])
                

            elif inp[2] == "privacy":
                boards[inp[1]].setPrivacy(inp[3])
                print("privacy changed to",inp[3])
 
            elif inp[2] == "ADD_MEMBER":
                if inp[1] in boards:
                    boards[inp[1]].addMember(inp[3])
                else : print("board does not exist")
                

            elif inp[2] == "REMOVE_MEMBER":
                if inp[1] in boards:
                    boards[inp[1]].removeMember(inp[3])
                else : print("board does not exist")
                
            else: print("enter valid command")
        




        elif inp[0] == "LIST":

            if inp[1] == "CREATE":
                boardId = inp[2]
                listName = inp[3]

                if boardId in boards:  #if board exists
                    print("list created",boards[boardId].createList(listName))
                else: print("Board does not exist")
                    


            elif inp[1] == "DELETE":
                k = 0
                for i in boards:
                    if i.isList(inp[2]):
                        i.deleteList(inp[2])
                        k = 1
                        break
                if not k:
                    print("\nlist or board not found\n")
                

            elif inp[2] == "name":
                k = 0
                for i in boards:
                    if i.isList(inp[1]):
                        i.list[inp[1]].setName(inp[3])
                        k = 1
                        break
                if not k:
                    print("list or board not found\n")
                




        elif inp[0] == "CARD":

            if inp[1] == "CREATE":
                k=0
                for i in boards:
                    if boards[i].isList(inp[2]):
                        print("card created",boards[i].list[inp[2]].createCard(inp[3]))
                        break
                if not k:
                    print("board or list not found\n")
                

            
            elif inp[1] == "DELETE":
                k=0
                for i in boards:
                    if boards[i].isCard(inp[2]) != -1:
                        k = boards[i].isCard
                        i.list[k].deleteCard(inp[2])    #i:boardID, k:listID
                        break
                if not k:
                    print("board or list not found\n")


            else:
                cardId = inp[1]
                k = 0
                for i in boards:
                    if boards[i].isCard(cardId) != -1:
                        listId = boards[i].isCard
                        break
                if not k:
                    print("invalid cardId\n")
                    
                if inp[2] == "ASSIGN":
                    i.list[listId].cards[cardId].assUser(inp[3])
                
                elif inp[2] == "UNASSIGN":
                    i.list[listId].cards[cardId].unAssUser()

                else:       #"MOVE:"
                    cardObj = i.list[listId].cards[cardId]   #get the card object
                    i.list[listId].deleteCard(cardId)    #delete card object
                    targList = inp[3]
                    k = 0
                    for j in boards:
                        if boards[j].isList(targList):
                            boards[j].list[targList].cards[cardId]=cardObj      #move card to target 
                            break
                    if not k:
                        print("board or list not found\n")


                    
                
        elif inp[0] == "SHOW":


            if len(inp) == 1:
                if not boards:
                    print("nothing to dispay")
                else:
                    for i in boards:
                        boards[i].displayBoard()


            elif inp[1] == "BOARD":
                if inp[2] in boards:
                    boards[inp[2]].displayBoard()

            elif inp[1] == "LIST":
                for i in boards:
                    if boards[i].isList(inp[2]):
                        boards[i].list[inp[2]].displayList()
                        break
            
            elif inp[1] == "CARD":
                for i in boards:
                    if boards[i].isCard(cardId) != -1:
                        k = boards[i].isCard
                        i.list[k].cards[inp[2]].displayCards()
                        break


        else:
            print("Enter valid command")
          

if __name__ == '__main__':
    main()








