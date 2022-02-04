# Iterando com loops em uma lista aninhada
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for lista in listas: # Aqui trabalhamos na lista em si
    for numero in lista: #Aqui trabalhamos em cada número da lista
        print(numero)

# Iterando com list comprehension em uma lista aninhada
[[print(valor) for valor in lista] for lista in listas] # O primeiro for a ser executado é o último a ser escritona ordem