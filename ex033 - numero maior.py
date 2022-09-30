a = int (input("adicione um numero"))
b = int (input("coloque um segundo numero"))
c = int (input("coloque um terceiro numero"))
#verificando quem e menor
menor = a
if b < a and b < c:
    menor= b
if c < a and c < b:
    menor = c
print ("O menor numero é {}".format(menor))
#verificar o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("o maior valo e {}".format(maior))

