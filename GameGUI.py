from Board import Board
from gameRules import GameRules

def start():
    playerOne = input('Digite o nome do jogador 1: ')
    playerTwo = input('Digite o nome do jogador 2: ')
    return playerOne,playerTwo

class GameGUI(GameRules):
    def __init__(self, playerone, playertwo):
        self.board = Board()
        self.boardToPlay = self.board.CreateBoard()
        super().__init__(self.boardToPlay) #passando o tabuleiro para o construtor de gameRules
        self.playerone = playerone
        self.playertwo = playertwo 
        self.turn = 0
        
    def play(self):
        print('mainBoard do gameGUI:\n',self.boardToPlay)
        self.board.showBoard(self.boardToPlay)
        if self.turn: 
            jogadaLinha = int(input(f'{self.playerone} digite o número da linha'))-1 #Indices de python
            jogadaColuna = int(input(f'{self.playerone} digite o número da Coluna'))-1
            self.turn = 1
        else:
            jogadaLinha = int(input(f'{self.playerone} digite o número da linha'))-1
            jogadaColuna = int(input(f'{self.playerone} digite o número da Coluna'))-1
        self.playturn(jogadaLinha, jogadaColuna, self.turn)
        self.board.showBoard(self.boardToPlay)

#Iniciando o jogo 
p1,p2 = start()
jogoPrincipal = GameGUI(p1,p2)
jogoPrincipal.play()