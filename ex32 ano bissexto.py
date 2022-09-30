from datetime import date
ano = int (input("Digite um ano: ou coloque 0 para analisar o ano presente"))
if ano ==0:
    ano= date.today().year
if (ano % 400 == 0) or (ano %4 ==0 and ano % 100 != 0 ):
    print("O ano {} e bissexto".format(ano))
else:
    print ("o ano {} nao e bissexto".format(ano))