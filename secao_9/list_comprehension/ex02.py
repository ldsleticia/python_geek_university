numeros = [1, 2, 3, 4, 5]

def dobro(numero):
    return numero * numero

res = [dobro(numero) for numero in numeros]
print(res)

print([numero * 2 for numero in [1, 2, 3, 4, 5]])