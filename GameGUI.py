from Board import Board
from gameRules import GameRules
from Player import Player

class GameGUI(): #todo jogo tem regras
    def __init__(self,player1,player2,turn, turnInverter):
        self.turn = turn
        self.turnInverter = turnInverter
        self.rules = GameRules()
        self.board = Board()
        self.boardToPlay = self.board.CreateBoard() #passando o tabuleiro para o construtor de gameRules
        self.player = Player(player1,player2) #o jogo TEM jogadores.
        self.TurnTime = 1
    
    def victory(self,player,pos):
        print(f'PARABENS, VITÓRIA DO {self.turn[self.TurnTime]}')
        print(f"Vitoria com a jogada na posicao: {pos}")
        return True
        

    def play(self, turn):
        if turn==1:
            jogadaLinha, jogadaColuna = self.player.playerComunicate(self.player.player1)
        elif turn ==2:
            jogadaLinha, jogadaColuna = self.player.playerComunicate(self.player.player2)
        elif turn == 3:
            jogadaLinha, jogadaColuna = self.player.player2.playerComunicate("bot")

        playValidate = self.rules.PlayValidation(jogadaLinha, jogadaColuna,self.boardToPlay) 
          
        if playValidate and self.rules.validRange(jogadaLinha,jogadaColuna, self.boardToPlay):
            self.rules.playturn(jogadaLinha, jogadaColuna, self.TurnTime, self.boardToPlay)
            winCondition = self.rules.detectVictory(jogadaLinha, jogadaColuna, self.TurnTime, self.boardToPlay)
            print("Condicao de vitoria:",winCondition)
            if winCondition:
                self.board.showBoard(self.boardToPlay)
                value = self.victory(self.turn[self.TurnTime],[jogadaLinha+1, jogadaColuna+1])
                if value:
                    return
                print("turno:", self.turnInverter)
            self.board.showBoard(self.boardToPlay)
            self.TurnTime = self.turnInverter[self.TurnTime] #Se a jogada for valida, troca o turno
        else:
            print('Jogada invalida! Tente de novo:')
        self.play(self.TurnTime)


 