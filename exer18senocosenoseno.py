from math import sin, cos, tan, radians
angulo = float (input("digite um ängulo: "))
sen =sin(radians(angulo))
print ("o ängulo {} possui seno = {:.2f} " .format (angulo, sen))
cos = cos(radians(angulo))
print ("o angulo {} possui cosseno = {: .2f}" .format (angulo, cos))
tag = tan(radians(angulo))
print ("o angulo {} possui tangente = {:.2f}" .format (angulo, tag))


