numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Qualquer número par módulo de é 2 == 0. 0 Em Python é == a False. not False == True
pares2 = [numero for numero in numeros if not numero % 2]

# Qualquer número ímpar módulo de 2 é == 1. 1 em Python é == True
impares2 = [numero for numero in numeros if numero % 2]

print(pares2)
print(impares2)
