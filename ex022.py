"Utilizando oerações com string (refazer)"
nome =str(input("Escreva seu nome completo: ")).strip()
print ("nome maisculos: {}" .format(nome.upper()))
print( "nome minusculo? {}".format(nome.lower()))
print("seu nome possue {}".format(len(nome) - nome.count(" ")))
separa = nome.split()
print("seu primeiro nome e {} e possue {} letras " .format(separa[0], len(separa[0])))