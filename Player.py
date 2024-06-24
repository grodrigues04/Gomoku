class Player():
    def __init__(self, player1, player2):
        self.player1 = player1
        if player2 != "bot":
            self.player2 = player2
            
        #self.turnPlayer = {0:playerone, 1:playertwo}
    def playerMove(self,jogadaLinha,JogadaColuna):
        return jogadaLinha,JogadaColuna
        
    def playerComunicate(self,turn_menssage):
        jogadaLinha = int(input(f'{turn_menssage} digite o número da linha'))-1 #Indices de python
        jogadaColuna = int(input(f'{turn_menssage} digite o número da Coluna'))-1
        return jogadaLinha, jogadaColuna

        