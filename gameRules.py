turnColor = {
    1: '\033[32m1\033[0m',
    2: '\033[34m2\033[0m',
    3: '\033[33m3\033[0m'
}


class GameRules():
    
    def PlayValidation(self, playerline, playercolum, tabuleiro):
        #Verificando se a posicao esta dentro dos limites do tabuleiro
        if 0 <= playerline <= 18 and  0 <= playercolum <=18: 
            if tabuleiro[playerline][playercolum] == ' ': #então a jogada é valida
                return True
            else:
                return False
    def playturn(self, playerline, playercolum, turnTime, tabuleiro):
        if turnTime==1:
            tabuleiro[playerline][playercolum] = '\033[32m1\033[0m'
        elif turnTime == 2:
            tabuleiro[playerline][playercolum] = '\033[34m2\033[0m'
        else:
            tabuleiro[playerline][playercolum] = '\033[33m3\033[0m'
            
    def validRange(self, x, y, tabuleiro):
        detector = 0 <= x < len(tabuleiro) and 0 <= y < len(tabuleiro[0])    
        return detector 
    
    def detectVictory(self, jogadaLinha, jogadaColuna, turnTime, tabuleiro):
        turn = turnColor[turnTime]
        def countDirection(deltaLinha, deltaColuna):
            count = 0
            linha, coluna = jogadaLinha, jogadaColuna
            while self.validRange(linha, coluna, tabuleiro) and tabuleiro[linha][coluna] == turn:
                count += 1
                linha += deltaLinha
                coluna += deltaColuna
            return count

        directions = [
            (1, 0), (-1, 0), # vertical
            (0, 1), (0, -1), # horizontal
            (1, 1), (-1, -1), # diagonal \
            (1, -1), (-1, 1) # diagonal /
        ]
        i = 0
        while i < len(directions):
            delta1 = directions[i] 
            delta2 = directions[i + 1]
            total_count = countDirection(*delta1) + countDirection(*delta2) - 1 # subtrai 1 porque a posição atual é contada duas vezes
            if total_count >= 5:
                return True
            i+=2 #primeiro pegamos so os valor de vertical, depois so os valores de horizonal...
        return False

        
