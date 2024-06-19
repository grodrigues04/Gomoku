turnColor = {
    0:'\033[34m0\033[0m',
    1:'\033[32m1\033[0m'
}
class GameRules():
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro
        
    def PlayValidation(self, playerline, playercolum):
        if self.tabuleiro[playerline][playercolum] != 0: #então a jogada é invalida
            return False
        else:
            return True
    def playturn(self, playerline, playercolum, turn):
        if turn:
            self.tabuleiro[playerline][playercolum] = '\033[32m1\033[0m'
        else:
            self.tabuleiro[playerline][playercolum] = '\033[34m0\033[0m'
    
    def detectVictory(self, jogadaLinha, jogadaColuna, turn):
        turn = turnColor[turn]
        #Verificando as diagonais 
        scoreUpperDigRT = 1
        scoreUpperDiaLR = 1
        scoreLowDiaLR = 1
        scoreLowDiaRL = 1
        ScoreLineLR = 1
        ScoreLineRL =1
        ScoreColumDown = 1
        ScoreColumUp = 1
        diagonal = 1
        while diagonal <= 5:
            #Diagonal de baixo esquerda para direita
            if self.tabuleiro[jogadaLinha+diagonal][jogadaColuna+diagonal] == turn: 
                 scoreLowDiaLR+=1
            #Diagonal de cima direita para esquerda
            if self.tabuleiro[jogadaLinha-diagonal][jogadaColuna-diagonal] == turn: 
                scoreUpperDigRT+=1
            #Diagonal de cima esquerda para a direita
            if self.tabuleiro[jogadaLinha-diagonal][jogadaColuna+diagonal] == turn:
                scoreUpperDiaLR+=1
            #Diagonal de baixo direita para esquerda
            if self.tabuleiro[jogadaLinha+diagonal][jogadaColuna-diagonal] == turn:
                scoreLowDiaRL+=1
            #Verificando a apenas a linha direita para esquerda
            if self.tabuleiro[jogadaLinha][jogadaColuna+diagonal] == turn:    
                ScoreLineLR+=1
            #Verificando a apenas a linha esquerda para direta
            if self.tabuleiro[jogadaLinha][jogadaColuna-diagonal] == turn:
                ScoreLineRL+=1
            #Verificando a apenas a coluna pra baixo
            if self.tabuleiro[jogadaLinha+1][jogadaColuna] == turn:
                ScoreColumDown +=1
            #Verificando a apenas a coluna pra cima
            if self.tabuleiro[jogadaLinha-1][jogadaColuna] == turn:
                ScoreColumUp +=1
            diagonal+=1
        scoreList = [scoreUpperDigRT, scoreUpperDiaLR, scoreLowDiaLR, scoreLowDiaRL, ScoreLineLR, ScoreLineRL,ScoreColumDown,ScoreColumUp]
        #print(scoreList)
        if 5 in scoreList: #Então, algumas das pontuções foi 5
            return True
        else:
            return False
        
