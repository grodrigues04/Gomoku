from Board import Board
from gameRules import judge

def start():
    playerOne = input('Digite o nome do jogador 1')
    playerTwo = input('Digite o nome do jogador 2')
    return playerOne,playerTwo

class GameGUI(Board):
    def __init__(self, playerone, playertwo):
        self.board = self.CreateBoard()
        self.gameJudge = judge(Board.CreateBoard(self))
        self.playerone = playerone
        self.playertwo = playertwo 
        self.turn = 0
        
    def play(self):
        if self.turn: 
            jogadaLinha = int(input(f'{self.playerone} digite o número da linha'))-1 #Indices de python
            jogadaColuna = int(input(f'{self.playerone} digite o número da Coluna'))-1
            self.turn = 1
        else:
            jogadaLinha = int(input(f'{self.playerone} digite o número da linha'))-1
            jogadaColuna = int(input(f'{self.playerone} digite o número da Coluna'))-1
        self.gameJudge.playturn(jogadaLinha, jogadaColuna, self.turn)


#Iniciando o jogo 
p1,p2 = start()
jogoPrincipal = GameGUI(p1,p2)
jogoPrincipal.play()