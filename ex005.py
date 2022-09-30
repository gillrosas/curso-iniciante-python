# Exercício 5: ler um número e achar o seu sucessor e seu antencessor

num = float(input('Digite um número: '))
sucessor = num + 0.1
ante = num - 0.1
print('o antecessor é: {},  e o seu sucessor: {}'.format(ante, sucessor))
