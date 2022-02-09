lista = []
numeros = 0

while len(lista) < 10:
    print("Digite dez números ")
    numeros = input()
    if len(lista) <= 10:
        lista.append(numeros)

for i in range(len(lista)):
    if i % 2 == 0:
        print(i)
