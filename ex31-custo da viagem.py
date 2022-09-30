#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float (input("Coloque a distäncia da sua viagem em KM"))
if distancia <= 200:
    valor = distancia*0.50
    print ("Voce vai percorrer {} Km e pagara {}reais ".format(distancia, valor))
else:
    valor2 = distancia*0.45
    print ("voce vai percorrer {} Km e pagara {}reais ".format(distancia,valor2))