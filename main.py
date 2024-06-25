#Iniciando o jogo
import GameGUI
from machine import Bot
def start():
    turn = {}
    turnInvert = {}
    
    playerOne = input('Digite o nome do jogador 1: ')
    turn[1] = playerOne
    print("Caso queira jogar contra um bot, digite 'bot' ")
    playerTwo = input('Digite o nome do jogador 2: ')
    if playerTwo== "bot":
        playerTwo = Bot(playerOne, "RANDOM")
        turn[3] = "bot"
        turnInvert[1] = 3
        turnInvert[3] = 1

    else:
        turn[2] = playerTwo
        turnInvert[2] = 1 
        turnInvert[1] = 2

        
    return playerOne, playerTwo, turn, turnInvert

p1, p2, turn, turnInvert = start()
jogoPrincipal = GameGUI.GameGUI(p1 ,p2, turn, turnInvert)
jogoPrincipal.play(1) #Jogador 1 comeca
