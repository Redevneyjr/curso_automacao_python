# Jogo de Adivinhação

import random
secretnumber = random.randint(1, 20)
print('estou pensando em um número de 1 a 20.')

for tentativas in range(1, 7):
    print('tente adivinhar o número')
    guess = int(input())

    if guess < secretnumber:
        print('sua tentativa foi muito baixa.')
    elif guess > secretnumber:
        print('sua tentativa foi muito alta.')
    else:
        break
if guess == secretnumber:
    print('muito bem ! você acertou o número em'  +  str(tentativas)  +  'tentativas')
else:
    print('que pena! você não conseguiu acertar o número que era:  ' + str(secretnumber))
