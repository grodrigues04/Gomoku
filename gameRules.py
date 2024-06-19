class GameRules():
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro
        
    def PlayValidation(self, playerline, playercolum):
        if self.tabuleiro[playerline][playercolum] != 0: #então a jogada é invalida
            return False
        else:
            return True
    def playturn(self, playerline, playercolum, turn):
        if turn:
            self.tabuleiro[playerline][playercolum] = '\033[32m1\033[0m'
        else:
            self.tabuleiro[playerline][playercolum] = '\033[34m2\033[0m'
    
