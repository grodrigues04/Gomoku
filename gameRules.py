turnColor = {
    0:'\033[34m0\033[0m',
    1:'\033[32m1\033[0m'
}


class GameRules():
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro
    
    def PlayValidation(self, playerline, playercolum):
        if 1<= playerline 
        if self.tabuleiro[playerline][playercolum] == ' ': #então a jogada é invalida
            return True
        else:
            return False
    def playturn(self, playerline, playercolum, turn):
        if turn:
            self.tabuleiro[playerline][playercolum] = '\033[32m1\033[0m'
        else:
            self.tabuleiro[playerline][playercolum] = '\033[34m0\033[0m'
            
    def validRange(self, x, y):
        detector = 0 <= x < len(self.tabuleiro) and 0 <= y < len(self.tabuleiro[0])    
        return detector 
    def detectVictory(self, jogadaLinha, jogadaColuna, turn):
        p = turn
        turn = turnColor[p]
        print(turn)
        
        # Inicialização das variáveis de pontuação
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
            if self.validRange(jogadaLinha + diagonalA, jogadaColuna + diagonalA):
                if self.tabuleiro[jogadaLinha + diagonalA][jogadaColuna + diagonalA] == turn:
                    scoreLowDiaLR += 1
                    diagonalA += 1
                else:
                    break
            else:
                break

        # Diagonal de cima direita para esquerda
        diagonalA = 1
        while diagonalA < 5:
            if self.validRange(jogadaLinha - diagonalA, jogadaColuna - diagonalA):
                if self.tabuleiro[jogadaLinha - diagonalA][jogadaColuna - diagonalA] == turn:
                    scoreUpperDiaRL += 1
                    diagonalA += 1
                else:
                    break
            else:
                break

        # Diagonal de cima esquerda para direita
        diagonalA = 1
        while diagonalA < 5:
            if self.validRange(jogadaLinha - diagonalA, jogadaColuna + diagonalA):
                if self.tabuleiro[jogadaLinha - diagonalA][jogadaColuna + diagonalA] == turn:
                    scoreUpperDiaLR += 1
                    diagonalA += 1
                else:
                    break
            else:
                break

        # Diagonal de baixo direita para esquerda
        diagonalA = 1
        while diagonalA < 5:
            if self.validRange(jogadaLinha + diagonalA, jogadaColuna - diagonalA):
                if self.tabuleiro[jogadaLinha + diagonalA][jogadaColuna - diagonalA] == turn:
                    scoreLowDiaRL += 1
                    diagonalA += 1
                else:
                    break
            else:
                break

        # Verificando a linha para a direita
        diagonalA = 1
        while diagonalA < 5:
            if self.validRange(jogadaLinha, jogadaColuna + diagonalA):
                if self.tabuleiro[jogadaLinha][jogadaColuna + diagonalA] == turn:
                    ScoreLineLR += 1
                    diagonalA += 1
                else:
                    break
            else:
                break

        # Verificando a linha para a esquerda
        diagonalA = 1
        while diagonalA < 5:
            if self.validRange(jogadaLinha, jogadaColuna - diagonalA):
                if self.tabuleiro[jogadaLinha][jogadaColuna - diagonalA] == turn:
                    ScoreLineRL += 1
                    diagonalA += 1
                else:
                    break
            else:
                break

        # Verificando a coluna para baixo
        diagonalA = 1
        while diagonalA < 5:
            if self.validRange(jogadaLinha + diagonalA, jogadaColuna):
                if self.tabuleiro[jogadaLinha + diagonalA][jogadaColuna] == turn:
                    ScoreColumDown += 1
                    diagonalA += 1
                else:
                    break
            else:
                break

        # Verificando a coluna para cima
        diagonalA = 1
        while diagonalA < 5:
            if self.validRange(jogadaLinha - diagonalA, jogadaColuna):
                if self.tabuleiro[jogadaLinha - diagonalA][jogadaColuna] == turn:
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

        
