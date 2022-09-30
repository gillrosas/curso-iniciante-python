"Ecrever um programa que leia um numero de 0 a 9999e mostra na dela cada um dos digitos separados"
num = int(input("escreva um numero "))
print("o numero analisado {}" .format(num))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print("unidade {}".format(unidade))
print ("dezena {}".format(dezena))
print ("centena {}".format(centena))
print("milhar {}" .format(milhar))
