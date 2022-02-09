lista = []
numeros = 0
while len(lista) < 6:
    print("Digite seis números ")
    numeros = input()
    if len(lista) <= 6:
        lista.append(numeros)
print(lista)
