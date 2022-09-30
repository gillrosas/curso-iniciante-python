#Exercício pintando parede
lar = float(input ('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
area = (lar * alt)
t= float(area / 2)
print ('a parede tem {} m2 e a quantidade de tinta para pintar e: {} L'.format(area, t))
