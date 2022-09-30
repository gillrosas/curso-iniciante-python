sal = float (input("coloque seu salario"))
if sal > 1250:
    sal = sal + (sal * 10 / 100)
    print("O seu sal[ario passou a ser {:.2f} reais".format(sal))
else:
    sal = sal + (sal* 15 / 100)
    print("o novo seu novo salario e {} reais".format(sal))
