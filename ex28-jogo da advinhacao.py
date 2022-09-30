"jogo da advinhacao"
jogador = int (input("o computador pensou em numero de 0 a 5, chute qual foi"))
from random import randint #randit para randomizar numero inteiro
from time import sleep #outra biblioteca do Python
computador = randint(0,5)
print("PROCESSANDO")
sleep(6)
if computador == jogador:
    print("parabens, voce acertou o numero ")
else:
    print("que pena, voce errou")


