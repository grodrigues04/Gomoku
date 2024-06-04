class Board():
    def __init__(self):
        self.line = 19
        self.colum = 19
    
    def CreateBoard(self):
        mainBoard = []
        lineControl = 0
        while lineControl < self.line:
            row = []
            columControl = 0
            while columControl < self.colum:
                row.append(0)
                columControl+=1
            mainBoard.append(row)
            lineControl+=1
        return mainBoard
    def showBoard(self,mainBoard):
        number = 1
        print('',f'\033[31m{number}\033[0m',end ="")
        number+=1
        while number <= self.line:
            numberPrint = f'\033[31m{number}\033[0m'
            if number <= 9:
                print('  ',numberPrint,end ="")
            else:
                print(' ',numberPrint,end ="")
            number+=1
        print()
        for linha in mainBoard:
            for item in linha:
                print(f' {item} |',end='') 
            print()
print()
teste = Board()
tabuleiro = teste.CreateBoard()
teste.showBoard(tabuleiro)

'''
 1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
'''

