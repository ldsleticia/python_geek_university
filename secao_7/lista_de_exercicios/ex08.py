lista = []

while len(lista) < 6:
    numeros = int(input('Digite dez números: '))
    lista.append(numeros)
print(lista[::-1])