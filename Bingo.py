import random

class Board:
    def __init__(self):
        self.position = {}
        self.playBoard = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]
        self.bingo = {
            "row" : [0,0,0,0,0],
            "col" : [0,0,0,0,0],
            "diagonal" : [0,0]
        }
        self.createBoard()
    
    def createBoard(self):
        choices = [i for i in range(1,26)]
        for i in range(5):
            for j in range(5):
                choice = random.choice(choices)
                self.playBoard[i][j] = choice
                choices.pop(choices.index(choice))
                self.position[choice] = (i,j)
    
    def updateBoard(self, val):
        x,y = self.position[val]
        self.playBoard[x][y] = 'X'
        self.updateBingo(x,y)
   
    def updateBingo(self, x, y):
        self.bingo["row"][x] += 1
        self.bingo["col"][y] += 1
        if x==y==2:
            self.bingo["diagonal"][0] += 1
            self.bingo["diagonal"][1] += 1
        elif x==y:
            self.bingo["diagonal"][0] += 1
        elif x+y == 4:
            self.bingo["diagonal"][1] += 1
   
    def checkBingo(self):
        return 5 in self.bingo["row"] or 5 in self.bingo["col"] or 5 in self.bingo["diagonal"]
 
class Player(Board):
    def __init__(self, name):
        self.name = name
        self.board = Board()
   
    def updatePlayerBoard(self, val):
        self.board.updateBoard(val)
   
    def checkBingo(self):
        return self.board.checkBingo()
 
class Game:
    def displayBoard(self, player1):
        board1 = player1.board.playBoard
        size = 20
        p1len = len(player1.name)
        print("Bingo sheet:")

        for i in range(5):
            for j in board1[i]:
                if j=='X':
                    print(f" {j}",end=" ")
                elif j>9:
                    print(j,end=" ")
                else:
                    print(f"0{j}",end=" ")
            print("      ",end="")
            print()
        print()
 
game = Game()
player1 = Player(name="player1")

while True:
    game.displayBoard(player1)
    val = int(input("The new number is: "))
    player1.updatePlayerBoard(val)
    game.displayBoard(player1)

    if player1.checkBingo():
        print("You won!")
        break
