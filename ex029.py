#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h"
 #mostre uma mensagem dizendo que ele foi multado."
#A multa vai custar R$7,00 por cada Km acima do limite."
speed = float (input("Coloque a velocidade do carro:"))
if speed > 80:
    multa = (speed - 80)*7
    print("sua velocidade ultrapassa o limite permitido", "vocë receber[a uma multa no valor de {:.2f} reais".format(multa))
print("Parabens, voce esta na velocidade permitida")