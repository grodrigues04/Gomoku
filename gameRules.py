class judge():
    def __init__(self,tabuleiro):
        self.tabuleiro = tabuleiro
    def playturn(self,playerline,playercolum,turn):
        #TO-DO: cores individuais para cada jogador 
        if turn:
            tabuleiro[playerline][playercolum] = '\033[32m{1}\033[0m'
        else:
            tabuleiro[playerline][playercolum] = '\033[34m{1}\033[0m'
