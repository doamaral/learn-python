__author__ = 'Lucas'

import random

opcao_play = "y"

while opcao_play == "y":
    acertou = False
    opcao_repeat = "y"
    sorted_num = random.randrange(1, 10, 1, int)
    print("cheat: %d" % sorted_num)
    chance = 3
    while (acertou == False or opcao_repeat == "y") and chance > 0:
        guess = int(input("Dê um chute de 1..10: "))
        if int(guess) == sorted_num:
            print("Parabéns, você acertou!!!")
            acertou = True
            opcao_repeat = "n"
        elif int(guess) > sorted_num:
            chance = chance - 1
            print("Mais baixo... você tem %d chances" % chance)
            opcao_repeat = input("Deseja continuar jogando? (y/n): ")
        else:
            chance = chance - 1
            print("Mais alto... você tem %d chances" % chance)
            opcao_repeat = input("Deseja continuar jogando? (y/n): ")
    opcao_play = input("Deseja um novo jogo? (y/n): ")
print("Obrigado por jogar Guessing Game")