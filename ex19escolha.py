from random import choice
n1 = str (input("coloco o nomeo do primeiro aluno "))
n2 = str (input("coloque o nome co segundo aluno"))
n3 = str (input ("coloque o nome do terceiro aluno"))
n4 = str (input("coloque o nome do quarto aluno"))
lista = [n1,n2, n3, n4]
escolhido = choice(lista)
print("o escolhido foi {}" .format (escolhido))

