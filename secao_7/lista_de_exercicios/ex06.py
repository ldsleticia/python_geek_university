lista = []

while len(lista) < 10:
    print("Digite dez números: ")
    numeros = int(input())
    lista.append(numeros)

max_number = max(lista)
min_number = min(lista)

print(lista)
print()
print(max_number)
print()
print(min_number)
