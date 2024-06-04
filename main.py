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
        print('coluna: ',end='')
        print('',f'\033[31m{number}\033[0m',end ="")
        number+=1
        #mostrando as colunas com numeros
        while number <= self.line:
            numberPrint = f'\033[31m{number}\033[0m'
            if number <= 9:
                print('  ',numberPrint,end ="")
            else:
                print(' ',numberPrint,end ="")
            number+=1
        print()
        linhaValor = 1
        #mostrando as linhas da matriz
        for linha in mainBoard:
            valorPrint = f'\033[31m{linhaValor}\033[0m'
            if linhaValor <10:
                print(f'Linha:{valorPrint} ',end='')
            else:
                print(f'Linha:{valorPrint}',end='')
            linhaValor+=1
            for item in linha:
                valores = f'\033[35m{item}\033[0m'
                print(f' {valores} |',end='') 
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

