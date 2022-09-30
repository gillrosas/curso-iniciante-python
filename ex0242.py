"criar um programa que leio nome de uma cidade e avaliar se tem um nome SANTO"
cidade = str(input("escreva o nome da cidade")).strip()
santo =cidade.upper()
print(santo[:5] == "SANTO")


