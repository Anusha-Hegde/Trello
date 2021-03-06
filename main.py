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
                key = inp[2]
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
                    if boards[i].isList(inp[2]):
                        boards[i].deleteList(inp[2])
                        k = 1
                        break
                if not k:
                    print("\nlist or board not found\n")
                

            elif inp[2] == "name":
                k = 0
                for i in boards:
                    if boards[i].isList(inp[1]):
                        boards[i].list[inp[1]].setName(inp[3])
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
                        k=1
                        break
                if not k:
                    print("board or list not found\n")
                

            
            elif inp[1] == "DELETE":
                k=0
                for i in boards:
                    if boards[i].isCard(inp[2]) != -1:
                        listId = boards[i].isCard
                        boards[i].list[listId].deleteCard(inp[2])    #i:boardID, k:listID
                        k=1
                        break
                if not k:
                    print("board or list not found\n")


            else:
                cardId = inp[1]
                k = 0
                for i in boards:
                    if boards[i].isCard(cardId) != -1:
                        listId = boards[i].isCard(cardId)
                        # print(listId)
                        k=1
                        break
                if not k:
                    print("invalid cardId\n")
                    continue
                    
                if inp[2] == "ASSIGN":
                    boards[i].list[listId].cards[cardId].assUser(inp[3])
                
                elif inp[2] == "UNASSIGN":
                    boards[i].list[listId].cards[cardId].unAssUser()

                elif inp[2] == "name":
                    boards[i].list[listId].cards[cardId].setName(inp[3])

                elif inp[2] == "description":
                    boards[i].list[listId].cards[cardId].setDescription(inp[3])

                elif inp[2] == "MOVE":       
                    cardObj = boards[i].list[listId].cards[cardId]   #get the card object
                    boards[i].list[listId].deleteCard(cardId)    #delete card object
                    targList = inp[3]
                    k = 0
                    for j in boards:
                        if boards[j].isList(targList):
                            boards[j].list[targList].cards[cardId]=cardObj  #move card to target
                            k=1       
                            break
                    if not k:
                        print("list not found\n")

                else : print("invalid command")


                    
                
        elif inp[0] == "SHOW":


            if len(inp) == 1:
                if not boards:
                    print("nothing to display")
                else:
                    for i in boards:
                        boards[i].displayBoard()


            elif inp[1] == "BOARD":
                if inp[2] in boards:
                    boards[inp[2]].displayBoard()
                else: print("board does not exist")

            elif inp[1] == "LIST":
                k=0
                for i in boards:
                    if boards[i].isList(inp[2]):
                        boards[i].list[inp[2]].displayList()
                        k=1
                        break
                if not k:
                    print("List does not exist")
            
            elif inp[1] == "CARD":
                k=0
                cardId = inp[2]
                for i in boards:
                    if boards[i].isCard(cardId) != -1:
                        listId = boards[i].isCard(cardId)
                        boards[i].list[listId].cards[cardId].displayCards()
                        k=1
                        break
                if not k:
                    print("card does not exist")


        else:
            print("Enter valid command")
          

if __name__ == '__main__':
    main()








