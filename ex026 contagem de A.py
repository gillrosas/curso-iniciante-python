"fazer um programa que leia uma frase no teclado e motre quantas vezes aparece a letra A"
nome = str(input("escreva uma frase:")).strip()
alto = nome.upper()
print("a frase {} possui: {} letter A".format(nome, alto.count("A")))
print("o A aparece pela primeira vez na posicao {} ".format(alto.find("A")+1))
print("e aparece  ultima vez na posicao {}".format(alto.rfind("A") +1 ))