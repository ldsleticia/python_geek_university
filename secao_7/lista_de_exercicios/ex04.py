lista = []
x = 0
y = 0

while len(lista) < 8:
    print("Digite até oito números: ")
    x = int(input())
    if len(lista) <= 10:
        lista.append(x)
print(lista)
