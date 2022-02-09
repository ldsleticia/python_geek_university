# O programa não sabe que chave é literalmente uma chav, o que o programa sabe é que ele precisa de uma chave para ser um dicionário
# Você poderia escrever batata ao invés de chave que ele entenderia que batata é a chave e que o valor a ser atribuído a batata
# É o valor que está após os :
numeros = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
}
quadrado = {chave: valor**2 for chave, valor in numeros.items()}

print(quadrado)

# Exemplificando o que foi explicado acima
# Vou pegar a chave 'a', colocá-la dentro de batata e o valor após o : em valor
# Valor também poderia ter qualquer nome aleatório como por exemplo hortelã
numeros = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
}
quadrado = {batata: valor**2 for batata, valor in numeros.items()}

print(quadrado)

# Exemplificando o que foi explicado acima
numeros = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
}
quadrado = {batata: hortela**2 for batata, hortela in numeros.items()}

print(quadrado)
