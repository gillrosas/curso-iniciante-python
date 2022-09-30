"ler um nome completo da pessoa e mostrar o primeiro e o ultimo nome"
nome = str(input("Escreva seu nome completo:")).strip()
fracionado = nome.split()
print ("o primeiro nome e {}".format(fracionado[0]))
print(" o ultimo nome e {}".format(fracionado[len(fracionado) -1]))
