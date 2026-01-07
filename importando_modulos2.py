# nós também podemos forçar a interrupção do programa, conforme o exemplo abaixo:
import sys

while True:
    print('Digite sair para terminar a execução do programa')
    resposta = input()
    if resposta == 'sair':
        sys.exit()
    print('Você digitou ' + resposta + ' e não "sair"')
