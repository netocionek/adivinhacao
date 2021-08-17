from random import randint
from time import sleep
computador = randint(0, 5)
print('--=--' * 10)
print('Bem vindo ao jogo da advinhação! ')
print('--=--' * 10)

print('Estou pensando em um número... Só um instante... ')
sleep(2)
jogador = int(input('Escolha um número de 0 a 5: '))
if jogador == computador:
    print('Você conseguiu me vencer! ')
else:
    print('Você perdeu!! ')
    print('Eu pensei no número {}, e não no número {}. '.format(computador, jogador))




