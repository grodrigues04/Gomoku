turnColor = {
    1: '\033[32m1\033[0m',
    2: '\033[34m0\033[0m',
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
        print(turn)
        #variáveis de pontuação para cada direcao.
        scoreUpperDiaRL = 1
        scoreUpperDiaLR = 1
        scoreLowDiaLR = 1
        scoreLowDiaRL = 1
        ScoreLineLR = 1
        ScoreLineRL = 1
        ScoreColumDown = 1
        ScoreColumUp = 1
        # Diagonal de baixo esquerda para direita
        diagonalA = 1
        while diagonalA < 5:
            if self.validRange(jogadaLinha + diagonalA, jogadaColuna + diagonalA,tabuleiro):
                if tabuleiro[jogadaLinha + diagonalA][jogadaColuna + diagonalA] == turn:
                    scoreLowDiaLR += 1
                    diagonalA += 1
                else:
                    break
            else:
                break

        # Diagonal de cima direita para esquerda
        diagonalA = 1
        while diagonalA < 5:
            if self.validRange(jogadaLinha - diagonalA, jogadaColuna - diagonalA, tabuleiro):
                if tabuleiro[jogadaLinha - diagonalA][jogadaColuna - diagonalA] == turn:
                    scoreUpperDiaRL += 1
                    diagonalA += 1
                else:
                    break
            else:
                break

        # Diagonal de cima esquerda para direita
        diagonalA = 1
        while diagonalA < 5:
            if self.validRange(jogadaLinha - diagonalA, jogadaColuna + diagonalA, tabuleiro):
                if tabuleiro[jogadaLinha - diagonalA][jogadaColuna + diagonalA] == turn:
                    scoreUpperDiaLR += 1
                    diagonalA += 1
                else:
                    break
            else:
                break

        # Diagonal de baixo direita para esquerda
        diagonalA = 1
        while diagonalA < 5:
            if self.validRange(jogadaLinha + diagonalA, jogadaColuna - diagonalA, tabuleiro):
                if tabuleiro[jogadaLinha + diagonalA][jogadaColuna - diagonalA] == turn:
                    scoreLowDiaRL += 1
                    diagonalA += 1
                else:
                    break
            else:
                break

        # Verificando a linha para a direita
        diagonalA = 1
        while diagonalA < 5:
            if self.validRange(jogadaLinha, jogadaColuna + diagonalA, tabuleiro):
                if tabuleiro[jogadaLinha][jogadaColuna + diagonalA] == turn:
                    ScoreLineLR += 1
                    diagonalA += 1
                else:
                    break
            else:
                break

        # Verificando a linha para a esquerda
        diagonalA = 1
        while diagonalA < 5:
            if self.validRange(jogadaLinha, jogadaColuna - diagonalA, tabuleiro):
                if tabuleiro[jogadaLinha][jogadaColuna - diagonalA] == turn:
                    ScoreLineRL += 1
                    diagonalA += 1
                else:
                    break
            else:
                break

        # Verificando a coluna para baixo
        diagonalA = 1
        while diagonalA < 5:
            if self.validRange(jogadaLinha + diagonalA, jogadaColuna, tabuleiro):
                if tabuleiro[jogadaLinha + diagonalA][jogadaColuna] == turn:
                    ScoreColumDown += 1
                    diagonalA += 1
                else:
                    break
            else:
                break

        # Verificando a coluna para cima
        diagonalA = 1
        while diagonalA < 5:
            if self.validRange(jogadaLinha - diagonalA, jogadaColuna, tabuleiro):
                if tabuleiro[jogadaLinha - diagonalA][jogadaColuna] == turn:
                    ScoreColumUp += 1
                    diagonalA += 1
                else:
                    break
            else:
                break

        # Verificando se alguma das pontuações atingiu 5
        scoreList = [scoreUpperDiaRL, scoreUpperDiaLR, scoreLowDiaLR, scoreLowDiaRL, ScoreLineLR, ScoreLineRL, ScoreColumDown, ScoreColumUp]
        print(scoreList)
        if 5 in scoreList:
            return True
        else:
            return False

        
