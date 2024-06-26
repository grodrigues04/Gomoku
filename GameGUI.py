from Board import Board
from gameRules import GameRules
from Player import Player

class GameGUI(): 
    def __init__(self,player1,player2,turn, turnInverter):
        self.turn = turn
        self.turnInverter = turnInverter
        self.rules = GameRules()
        self.board = Board()
        self.boardToPlay = self.board.CreateBoard() 
        self.player = Player(player1,player2) 
        self.TurnTime = 1
        
        self.board.showBoard(self.boardToPlay)  #Mostrando o tabuleiro assim que o jogo inicar
    
    def victory(self, player, pos):
        print(f'PARABENS, VITÓRIA DO {player}')
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
            if winCondition:
                self.board.showBoard(self.boardToPlay)
                value = self.victory(self.turn[self.TurnTime],[jogadaLinha+1, jogadaColuna+1])
                if value:
                    return #para o codigo
            self.board.showBoard(self.boardToPlay)
            self.TurnTime = self.turnInverter[self.TurnTime] #Se a jogada for valida, troca o turno
        else:
            print('Jogada invalida! Tente de novo:')
        self.play(self.TurnTime)


 