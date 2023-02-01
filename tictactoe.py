
class ticTacToe:
    def __init__(self):
        self.gameField = []
        
    def createField(self):
        count = 1
        for i in range(3):
            row = []
            for j in range(3):
                row.append(str(count))
                count +=1
            self.gameField.append(row)
    
    def drawField(self):
        for i in range(3):
            print(self.gameField[i])
            
    def gamePlay(self, number, player):
        for i in range(3):
            for j in range(3):
                if self.gameField[i][j] == number:
                    self.gameField[i][j] = player
            
    def checkWin(self, XorO):
        win = False
        
        #check row
        for i in range(3):
            win = True
            for j in range(3):
                if self.gameField[i][j] != XorO:
                    win = False
                    break
            if win:
                return win
        
        #check column
        for i in range(3):
            win = True
            for j in range(3):
                if self.gameField[j][i] != XorO:
                    win = False
                    break
            if win:
                return win
        
        #check diagonal
        for i in range(3):
            win = True
            if self.gameField[i][i] != XorO:
                win = False
                break
        if win:
            return win
            
        for i in range(3):
            win = True
            if self.gameField[i][2 - i] != XorO:
                win = False
                break
        if win:
            return win
        
        return win
    
    def checkDraw(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.gameField[i][j] == 'x' or self.gameField[i][j] == 'o':
                    count += 1
        if count == 9:
            return True
        else:
            return False
        
    def start(self):
        self.createField()
        self.drawField()
        
        player = 'x'
        count = 0
        
        while not self.checkWin(player):
            
            if count % 2 == 0:
                player = 'x'
            else:
                player = 'o'
                
            print(player)
            position = input('Input position ')
            
            self.gamePlay(position, player)
            self.drawField()
            count += 1
            
            if self.checkDraw() and not self.checkWin(player):
                print('Draw')
                break
            
        if self.checkWin(player) :
            print('winner', player)
        
        
        
ticTacToe().start()