lista = []
numeros = 0

while len(lista) < 10:
    print("Digite dez números ")
    numeros = int(input())
    lista.append(numeros)
print(lista)
print(f"O maior numero da lista é {max(lista)}")
print()
print(f"O índice desse número é {lista.index(max(lista))}")
