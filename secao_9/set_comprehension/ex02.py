# Números de 0 até 9 sendo elevados ao quadrado
# Set comprehension é desordenado, por isso os valores fora de ordem
numeros = {x**2 for x in range(10)}
print(numeros)

# Dicionário
numeros = {x: x**2 for x in range(10)}
print(numeros)
