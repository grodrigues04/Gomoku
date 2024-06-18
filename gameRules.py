class GameRules():
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro
    def playturn(self, playerline, playercolum, turn):
        #TO-DO: cores individuais para cada jogador 
        if turn:
            self.tabuleiro[playerline][playercolum] = '\033[32m1\033[0m'
        else:
            self.tabuleiro[playerline][playercolum] = '\033[34m2\033[0m'
