lista = []
numeros = 0
while len(lista) < 6:
    numeros = int(input("Digite seis números pares: "))
    if numeros % 2 != 0:
        print("Esse não é um número válido")
    else:
        lista.append(numeros)

print(lista[::-1])
