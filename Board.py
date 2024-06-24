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
                row.append(" ")
                columControl += 1
            mainBoard.append(row)
            lineControl += 1
        return mainBoard

    def showBoard(self, mainBoard):
        number = 1
        print("coluna: ", end="")
        print("", f"\033[31m{number}\033[0m", end="")
        number += 1
        # mostrando as colunas com numeros
        while number <= self.line:
            numberPrint = f"\033[31m{number}\033[0m"
            if number <= 9:
                print("  ", numberPrint, end="")
            else:
                print(" ", numberPrint, end="")
            number += 1
        print()
        linhaValor = 1
        # mostrando as linhas da matriz
        for linha in mainBoard:
            valorPrint = f"\033[31m{linhaValor}\033[0m"
            if linhaValor < 10:
                print(f"Linha:{valorPrint} ", end="")
            else:
                print(f"Linha:{valorPrint}", end="")
            linhaValor += 1
            for item in linha:
                valores = f"\033[35m{item}\033[0m"
                print(f" {valores} |", end="")
            print()
            print("         ", end="")  # 8 spaces
            print("--|", end="")
            quadrado = 1
            while quadrado < self.line:
                print("---|", end="")
                quadrado += 1
            print()
        print()
