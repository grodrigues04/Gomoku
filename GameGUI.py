from Board import Board
from gameRules import GameRules

turnInverte = {
    0:1,
    1:0
}

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
        self.turn = 1
        

    def play(self):
        if self.turn: 
            jogadaLinha = int(input(f'{self.playerone} digite o número da linha'))-1 #Indices de python
            jogadaColuna = int(input(f'{self.playerone} digite o número da Coluna'))-1
            playValidate = self.PlayValidation(jogadaLinha, jogadaColuna)
        else:
            jogadaLinha = int(input(f'{self.playertwo} digite o número da linha'))-1
            jogadaColuna = int(input(f'{self.playertwo} digite o número da Coluna'))-1
            playValidate = self.PlayValidation(jogadaLinha, jogadaColuna)
            
        if playValidate:
            self.playturn(jogadaLinha, jogadaColuna, self.turn)
            self.board.showBoard(self.boardToPlay)
            self.turn = turnInverte[self.turn] #Se a jogada for valida, troca o turno
        else:
            print('Jogada invalida! Já existe uma peça nessa posição')
        self.play()

#Iniciando o jogo 
p1,p2 = start()
jogoPrincipal = GameGUI(p1,p2)
jogoPrincipal.play()