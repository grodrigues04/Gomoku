from random import randint
from Player import Player
class Bot(Player): #todo bot tambem e um jogador
    def __init__(self, player1, player2):
        super().__init__(player1, player2)
        
    def bot_move(self):
        jogadaLinha = randint(0, 18)
        jogadaColuna = randint(0, 18)
        print(f"Bot jogou na linha {jogadaLinha+1}, e coluna {jogadaColuna+1}")
        return jogadaLinha, jogadaColuna

    def playerComunicate(self, turn_message):
        jogadaLinha, jogadaColuna = self.bot_move()  
        return jogadaLinha, jogadaColuna
        